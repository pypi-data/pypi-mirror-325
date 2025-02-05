import inspect
from typing import Any, Set, Type, Union, get_args, get_origin

from pydantic import BaseModel


def generate_model_docs(
    model: Type[BaseModel], processed_models: Set[Type[BaseModel]] | None = None
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

    # Get field information
    for field_name, field in model.model_fields.items():
        # Get field properties
        field_type, refs = get_type_str(field.annotation, processed_models)
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

    return html


def get_type_str(
    annotation: Any, known_models: Set[Type[BaseModel]]
) -> tuple[str, Set[Type[BaseModel]]]:
    """
    Gets a readable string representation of a type annotation,
    including nested types and model references.
    Returns the type string and any referenced models.
    """
    if annotation is None:
        return "Any", set()

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
