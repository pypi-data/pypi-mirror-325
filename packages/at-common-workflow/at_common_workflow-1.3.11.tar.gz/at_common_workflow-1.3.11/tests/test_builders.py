import pytest
from at_common_workflow.builders.workflow import WorkflowBuilder
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: int
    b: int

class AddOutputModel(BaseModel):
    result: int

async def execute_add(input: AddInputModel) -> AddOutputModel:
    return AddOutputModel(result=input.a + input.b)

@pytest.mark.asyncio
async def test_task_builder_initialization():
    workflow = (WorkflowBuilder()
        .add_task("add_task")
            .with_input_model(AddInputModel)
            .with_output_model(AddOutputModel)
            .with_execute_func(execute_func=execute_add)
            .with_constant_arg("a", 5)
            .with_constant_arg("b", 3)
        .store_result("add_task_result", "result")
        .build()
    )

    # Assert that the workflow is not None
    assert workflow is not None

    # Assert that the task was added to the workflow
    assert len(workflow.nodes) == 1  # Assuming only one task is added

    # Assert that the task's name is correct
    task_node = workflow.nodes[0]
    assert task_node.task.name == "add_task"

    # Assert that the input model is set correctly
    assert task_node.task.input_model is AddInputModel

    # Assert that the output model is set correctly
    assert task_node.task.output_model is AddOutputModel

    # Assert that the constant arguments are mapped correctly
    assert task_node.argument_mappings["a"].value == 5
    assert task_node.argument_mappings["b"].value == 3

    # Assert that the result mapping is set correctly
    assert task_node.result_mapping.context_key == "add_task_result"

@pytest.mark.asyncio
async def test_task_builder_with_description():
    workflow = (WorkflowBuilder()
        .add_task("add_task")
            .with_description("Adds two numbers")
            .with_input_model(AddInputModel)
            .with_output_model(AddOutputModel)
            .with_execute_func(execute_add)
            .with_constant_arg("a", 5)
            .with_constant_arg("b", 3)
        .store_result("result")
        .build()
    )
    
    assert workflow.nodes[0].task.description == "Adds two numbers"

@pytest.mark.asyncio
async def test_task_builder_with_context_arg():
    workflow = (WorkflowBuilder()
        .add_task("first_task")
            .with_input_model(AddInputModel)
            .with_output_model(AddOutputModel)
            .with_execute_func(execute_add)
            .with_constant_arg("a", 5)
            .with_constant_arg("b", 3)
        .store_result("first_result", "result")
        .add_task("second_task")
            .with_input_model(AddInputModel)
            .with_output_model(AddOutputModel)
            .with_execute_func(execute_add)
            .with_context_arg("a", "first_result")
            .with_constant_arg("b", 2)
        .store_result("final_result", "result")
        .build()
    )
    
    assert len(workflow.nodes) == 2
    second_task = workflow.nodes[1]
    assert second_task.argument_mappings["a"].value == "$first_result"
    assert second_task.argument_mappings["b"].value == 2

@pytest.mark.asyncio
async def test_task_builder_invalid_input_model():
    class InvalidModel:  # Not a Pydantic model
        pass
    
    with pytest.raises(TypeError, match="input_model must be a Pydantic BaseModel class"):
        (WorkflowBuilder()
            .add_task("invalid_task")
                .with_input_model(InvalidModel)
        )

@pytest.mark.asyncio
async def test_task_builder_missing_required_components():
    # Missing input model
    with pytest.raises(ValueError, match="Input model must be defined"):
        (WorkflowBuilder()
            .add_task("incomplete_task")
                .with_output_model(AddOutputModel)
                .with_execute_func(execute_add)
                .with_constant_arg("a", 1)
                .with_constant_arg("b", 2)
            .store_result("result")
        )
    
    # Missing execute function
    with pytest.raises(ValueError, match="Execute function must be defined"):
        (WorkflowBuilder()
            .add_task("incomplete_task")
                .with_input_model(AddInputModel)
                .with_output_model(AddOutputModel)
                .with_constant_arg("a", 1)
                .with_constant_arg("b", 2)
            .store_result("result")
        )

@pytest.mark.asyncio
async def test_task_builder_invalid_constant_arg():
    with pytest.raises(ValueError, match="Constant argument .* looks like a context reference"):
        (WorkflowBuilder()
            .add_task("invalid_task")
                .with_input_model(AddInputModel)
                .with_output_model(AddOutputModel)
                .with_execute_func(execute_add)
                .with_constant_arg("a", "$invalid_ref")
        )

@pytest.mark.asyncio
async def test_multiple_tasks_workflow():
    # Create a more complex workflow with multiple tasks
    workflow = (WorkflowBuilder()
        .add_task("task1")
            .with_input_model(AddInputModel)
            .with_output_model(AddOutputModel)
            .with_execute_func(execute_add)
            .with_constant_arg("a", 5)
            .with_constant_arg("b", 3)
        .store_result("result1", "result")
        .add_task("task2")
            .with_input_model(AddInputModel)
            .with_output_model(AddOutputModel)
            .with_execute_func(execute_add)
            .with_context_arg("a", "result1")
            .with_constant_arg("b", 2)
        .store_result("final_result", "result")
        .build()
    )
    
    assert len(workflow.nodes) == 2
    
    # Verify first task
    task1 = workflow.nodes[0]
    assert task1.task.name == "task1"
    assert task1.argument_mappings["a"].value == 5
    assert task1.argument_mappings["b"].value == 3
    assert task1.result_mapping.context_key == "result1"
    assert task1.result_mapping.result_path == "result"
    
    # Verify second task
    task2 = workflow.nodes[1]
    assert task2.task.name == "task2"
    assert task2.argument_mappings["a"].value == "$result1"
    assert task2.argument_mappings["b"].value == 2
    assert task2.result_mapping.context_key == "final_result"
    assert task2.result_mapping.result_path == "result"

@pytest.mark.asyncio
async def test_task_builder_invalid_output_model():
    class InvalidModel:  # Not a Pydantic model
        pass
    
    with pytest.raises(TypeError, match="output_model must be a Pydantic BaseModel class"):
        (WorkflowBuilder()
            .add_task("invalid_task")
                .with_input_model(AddInputModel)
                .with_output_model(InvalidModel)
        )

@pytest.mark.asyncio
async def test_task_builder_chaining():
    # Test that all builder methods return self for proper chaining
    builder = WorkflowBuilder().add_task("chain_task")
    
    # Test each method returns the builder instance
    assert builder.with_description("test") is builder
    assert builder.with_input_model(AddInputModel) is builder
    assert builder.with_output_model(AddOutputModel) is builder
    assert builder.with_execute_func(execute_add) is builder
    assert builder.with_constant_arg("a", 1) is builder
    assert builder.with_context_arg("b", "some_key") is builder

@pytest.mark.asyncio
async def test_task_builder_result_paths():
    # Create a more complex output model for testing result paths
    class ComplexOutputModel(BaseModel):
        value: int
        nested: dict
        items: list

    async def complex_execute(input: AddInputModel) -> ComplexOutputModel:
        return ComplexOutputModel(
            value=input.a + input.b,
            nested={"result": input.a * input.b},
            items=[input.a, input.b]
        )

    workflow = (WorkflowBuilder()
        .add_task("complex_task")
            .with_input_model(AddInputModel)
            .with_output_model(ComplexOutputModel)
            .with_execute_func(complex_execute)
            .with_constant_arg("a", 5)
            .with_constant_arg("b", 3)
        .store_result("result1", "value")  # Store just the value field
        .add_task("nested_task")
            .with_input_model(AddInputModel)
            .with_output_model(ComplexOutputModel)
            .with_execute_func(complex_execute)
            .with_constant_arg("a", 2)
            .with_constant_arg("b", 4)
        .store_result("result2", "nested.result")  # Store nested field
        .build()
    )
    
    assert len(workflow.nodes) == 2
    assert workflow.nodes[0].result_mapping.result_path == "value"
    assert workflow.nodes[1].result_mapping.result_path == "nested.result"

@pytest.mark.asyncio
async def test_task_builder_duplicate_task_names():
    workflow_builder = WorkflowBuilder()
    
    # Add first task
    workflow_builder.add_task("same_name") \
        .with_input_model(AddInputModel) \
        .with_output_model(AddOutputModel) \
        .with_execute_func(execute_add) \
        .with_constant_arg("a", 1) \
        .with_constant_arg("b", 2) \
        .store_result("result1")
    
    # Add second task with same name
    workflow_builder.add_task("same_name") \
        .with_input_model(AddInputModel) \
        .with_output_model(AddOutputModel) \
        .with_execute_func(execute_add) \
        .with_constant_arg("a", 3) \
        .with_constant_arg("b", 4) \
        .store_result("result2")
    
    # Build should succeed as duplicate names are allowed
    workflow = workflow_builder.build()
    assert len(workflow.nodes) == 2
    assert workflow.nodes[0].task.name == "same_name"
    assert workflow.nodes[1].task.name == "same_name"

class UserInputModel(BaseModel):
    user_id: str
    user_data: dict

class UserOutputModel(BaseModel):
    processed: bool
    data: dict

async def process_user(input: UserInputModel) -> UserOutputModel:
    return UserOutputModel(
        processed=True,
        data={"id": input.user_id, **input.user_data}
    )

@pytest.mark.asyncio
async def test_task_builder_context_arg_variations():
    """Test different ways of using with_context_arg"""
    
    # Build workflow with both single and dictionary context mappings
    workflow = (WorkflowBuilder()
        .add_task("process_user")
            .with_input_model(UserInputModel)
            .with_output_model(UserOutputModel)
            .with_execute_func(process_user)
            # Test single value context mapping
            .with_context_arg("user_id", "user.id")
            # Test dictionary context mapping
            .with_context_arg("user_data", {
                "role": "user.role",
                "settings": "user.settings",
                "preferences": "user.prefs"
            })
        .store_result("result")
        .build()
    )

    # Verify argument mappings were created correctly
    process_task = workflow.nodes[0]
    
    # Check single value mapping
    assert process_task.argument_mappings["user_id"].value == "$user.id"
    
    # Check dictionary mapping
    user_data_mapping = process_task.argument_mappings["user_data"]
    assert user_data_mapping.dict_mapping == {
        "role": "$user.role",
        "settings": "$user.settings",
        "preferences": "$user.prefs"
    }
    
    # Test actual execution
    workflow.context.set("user.id", "123")
    workflow.context.set("user.role", "admin")
    workflow.context.set("user.settings", {"theme": "dark"})
    workflow.context.set("user.prefs", {"notifications": True})
    
    # Execute workflow
    context = await workflow.execute()
    
    # Verify results
    result = context.get("result")
    assert result.processed == True
    assert result.data["id"] == "123"
    assert result.data["role"] == "admin"
    assert result.data["settings"] == {"theme": "dark"}
    assert result.data["preferences"] == {"notifications": True}

@pytest.mark.asyncio
async def test_task_builder_context_arg_dollar_prefix():
    """Test that dollar prefix handling works correctly"""
    workflow = (WorkflowBuilder()
        .add_task("process_user")
            .with_input_model(UserInputModel)
            .with_output_model(UserOutputModel)
            .with_execute_func(process_user)
            # Test with and without dollar prefix
            .with_context_arg("user_id", "$user.id")
            .with_context_arg("user_data", {
                "role": "$user.role",
                "settings": "user.settings"  # No dollar prefix
            })
        .store_result("result")
        .build()
    )

    process_task = workflow.nodes[0]
    
    # Both should have dollar prefix in final mapping
    assert process_task.argument_mappings["user_id"].value == "$user.id"
    assert process_task.argument_mappings["user_data"].dict_mapping == {
        "role": "$user.role",
        "settings": "$user.settings"
    }

@pytest.mark.asyncio
async def test_task_builder_context_arg_nested_paths():
    """Test that deeply nested context paths work correctly"""
    workflow = (WorkflowBuilder()
        .add_task("process_user")
            .with_input_model(UserInputModel)
            .with_output_model(UserOutputModel)
            .with_execute_func(process_user)
            .with_context_arg("user_id", "users.current.id")
            .with_context_arg("user_data", {
                "role": "users.current.roles.primary",
                "settings": "users.current.preferences.settings"
            })
        .store_result("result")
        .build()
    )

    # Set up nested context
    workflow.context.set("users.current.id", "123")
    workflow.context.set("users.current.roles.primary", "admin")
    workflow.context.set("users.current.preferences.settings", {"theme": "dark"})
    
    # Execute workflow
    context = await workflow.execute()
    
    # Verify results
    result = context.get("result")
    assert result.processed == True
    assert result.data["id"] == "123"
    assert result.data["role"] == "admin"
    assert result.data["settings"] == {"theme": "dark"}