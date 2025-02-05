import inspect
from typing import (
    Any,
    Set,
    Type,
    Union,
    get_args,
    get_origin,
    get_type_hints,
    Optional,
    List,
)

from pydantic import BaseModel, Field


def generate_model_docs(
    model: Type[BaseModel],
    processed_models: Set[Type[BaseModel]] | None = None,
    with_style: bool = False,
) -> str:
    """
    Generates HTML documentation for a Pydantic model including field titles,
    descriptions, and types. Handles nested models recursively.

    Args:
        model: A Pydantic BaseModel class
        processed_models: Set of already processed models to avoid cycles

    Returns:
        str: HTML documentation for the model and its referenced models
    """
    if processed_models is None:
        processed_models = set()

    if model in processed_models:
        return ""

    processed_models.add(model)
    referenced_models = set()

    # Get model details
    model_name = model.__name__
    model_doc = inspect.getdoc(model) or ""

    # Start HTML template
    html = f"""
    <div class="model-docs" id="{model_name.lower()}">
        <h2 class="model-title">{model_name}</h2>
        <p class="model-description">{model_doc}</p>
        
        <table class="field-table">
            <thead>
                <tr>
                    <th>Field</th>
                    <th>Type</th>
                    <th>Description</th>
                    <th>Required</th>
                    <th>Default</th>
                </tr>
            </thead>
            <tbody>
    """

    # Resolve annotations properly to handle forward references
    resolved_annotations = get_type_hints(model, globalns=globals(), localns=locals())

    # Get field information
    for field_name, field in model.model_fields.items():
        # Use the resolved annotation instead of field.annotation
        field_annotation = resolved_annotations.get(field_name, field.annotation)

        # Get field properties
        field_type, refs = get_type_str(field_annotation, processed_models)
        referenced_models.update(refs)
        description = field.description or ""
        required = "Yes" if field.is_required else "No"

        # Handle default value display
        if field.default is None and not field.is_required:
            default = "None"
        elif field.default_factory is not None:
            default = f"{field.default_factory.__name__}()"
        elif field.default is not None:
            default = str(field.default)
        else:
            default = "-"

        # Add field row
        html += f"""
                <tr>
                    <td>{field_name}</td>
                    <td><code>{field_type}</code></td>
                    <td>{description}</td>
                    <td>{required}</td>
                    <td><code>{default}</code></td>
                </tr>
        """

    # Close current model documentation
    html += """
            </tbody>
        </table>
    </div>
    """

    # Generate documentation for referenced models
    for ref_model in referenced_models:
        if ref_model not in processed_models:
            html += generate_model_docs(ref_model, processed_models)

    if with_style:
        html += get_style()

    return html


def get_type_str(
    annotation: Any, known_models: Set[Type[BaseModel]]
) -> tuple[str, Set[Type[BaseModel]]]:
    """
    Gets a readable string representation of a type annotation,
    including nested types and model references.
    Returns the type string and any referenced models.
    """
    referenced_models = set()
    origin = get_origin(annotation)
    args = get_args(annotation)

    # Check if it's a Pydantic model
    if inspect.isclass(annotation) and issubclass(annotation, BaseModel):
        referenced_models.add(annotation)
        return (
            f'<a href="#{annotation.__name__.lower()}">{annotation.__name__}</a>',
            referenced_models,
        )

    if origin is None:
        return getattr(annotation, "__name__", str(annotation)), referenced_models
    elif origin is Union:
        # Handle Optional types
        non_none_args = [arg for arg in args if arg is not type(None)]
        if len(non_none_args) == 1:
            type_str, refs = get_type_str(non_none_args[0], known_models)
            referenced_models.update(refs)
            return f"Optional[{type_str}]", referenced_models
        return (
            f"Union[{', '.join(get_type_str(arg, known_models)[0] for arg in args)}]",
            referenced_models,
        )
    elif origin is list:
        # Handle List types
        type_str, refs = get_type_str(args[0], known_models)
        referenced_models.update(refs)
        return f"List[{type_str}]", referenced_models
    elif origin is dict:
        # Handle Dict types
        key_str, key_refs = get_type_str(args[0], known_models)
        val_str, val_refs = get_type_str(args[1], known_models)
        referenced_models.update(key_refs)
        referenced_models.update(val_refs)
        return f"Dict[{key_str}, {val_str}]", referenced_models
    else:
        # Handle other generic types
        return (
            f"{origin.__name__}[{', '.join(get_type_str(arg, known_models)[0] for arg in args)}]",
            referenced_models,
        )


def get_style():
    return """
        <style>
            .model-docs {
                font-family: system-ui, -apple-system, sans-serif;
                margin: 2rem;
                scroll-margin-top: 2rem;
            }
            .model-title {
                color: #2D3748;
                margin-bottom: 1rem;
            }
            .model-description {
                color: #4A5568;
                margin-bottom: 2rem;
            }
            .field-table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 2rem;
            }
            .field-table th,
            .field-table td {
                padding: 0.75rem;
                text-align: left;
                border-bottom: 1px solid #E2E8F0;
            }
            .field-table th {
                background-color: #F7FAFC;
                font-weight: 600;
                color: #4A5568;
            }
            .field-table td code {
                background-color: #EDF2F7;
                padding: 0.2rem 0.4rem;
                border-radius: 0.25rem;
                font-family: monospace;
            }
            .field-table td a {
                color: #4A5568;
                text-decoration: none;
                border-bottom: 1px dashed #4A5568;
            }
            .field-table td a:hover {
                color: #2D3748;
                border-bottom-style: solid;
            }
        </style>
        """


# Test Models
class Car(BaseModel):
    """Details about a car."""

    make: str = Field(description="The manufacturer of the car")
    price: int = Field(description="The price of the car in dollars")


class User(BaseModel):
    """A user in the system."""

    id: int = Field(description="Unique identifier for the user")
    username: str = Field(description="User's login name")
    email: str = Field(description="User's email address")
    full_name: Union[str, None] = Field(None, description="User's full name")
    age: Union[int, None] = Field(None, description="User's age in years")
    tags: list[str] = Field(default_factory=list, description="List of user tags")
    car: Union["Car", None] = Field(
        None, description="User's car details"
    )  # ForwardRef


# Generate documentation
docs = generate_model_docs(User, with_style=True)

# Save to file
with open("user_model_docs.html", "w") as f:
    f.write(docs)
