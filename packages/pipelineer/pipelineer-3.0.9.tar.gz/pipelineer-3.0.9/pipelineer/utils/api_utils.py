import os
import json

def map_api_field_type(avro_type):
    """
    Mapea el tipo definido en el esquema Avro de API a un tipo JSON simplificado.
    """
    if isinstance(avro_type, dict):
        logical = avro_type.get("logicalType")
        if logical == "decimal":
            return "numeric"
        elif logical == "datetime":
            return "datetime"
        else:
            return "string"
    elif isinstance(avro_type, str):
        if avro_type.lower() in ["long", "int"]:
            return "int"
        elif avro_type.lower() in ["double", "float"]:
            return "numeric"
        else:
            return "string"
    else:
        return "string"

def process_api_schema_file(json_file_path, avro_output_folder, json_output_folder):
    """
    Procesa un archivo JSON de API: guarda el esquema Avro en .avsc y genera el mapeo JSON.
    """
    with open(json_file_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    
    # Se usa la propiedad "name" del esquema para nombrar los archivos (en minúsculas)
    schema_name = schema.get("name", "unknown").lower()
    
    # Guardar el esquema Avro (.avsc)
    if not os.path.isdir(avro_output_folder):
        os.makedirs(avro_output_folder)
    avro_file_path = os.path.join(avro_output_folder, f"{schema_name}.avsc")
    with open(avro_file_path, 'w', encoding='utf-8') as avro_file:
        json.dump(schema, avro_file, indent=4)
    
    # Generar el mapeo JSON: para cada campo se mapea un tipo simplificado
    field_mappings = {}
    for field in schema.get("fields", []):
        field_name = field.get("name")
        field_type = field.get("type")
        # Si el tipo es una lista (por ejemplo, ["null", "string"]), se descarta "null"
        if isinstance(field_type, list):
            non_null_types = [t for t in field_type if t != "null"]
            field_type = non_null_types[0] if non_null_types else "string"
        json_type = map_api_field_type(field_type)
        field_mappings[field_name.upper()] = json_type
    
    if not os.path.isdir(json_output_folder):
        os.makedirs(json_output_folder)
    mapping_file_path = os.path.join(json_output_folder, f"{schema_name}.json")
    with open(mapping_file_path, 'w', encoding='utf-8') as mapping_file:
        json.dump(field_mappings, mapping_file, indent=4)
    
    print(f"Generado Avro: {avro_file_path}")
    print(f"Generado JSON: {mapping_file_path}")

def process_api_schemas(api_folder, avro_output_folder, json_output_folder):
    """
    Procesa todos los archivos JSON en la carpeta de API y genera
    los archivos Avro (.avsc) y JSON de mapeo correspondientes.
    """
    if not os.path.isdir(api_folder):
        raise ValueError(f"La carpeta de API no existe: {api_folder}")
    
    json_files = [f for f in os.listdir(api_folder) if f.lower().endswith('.json')]
    if not json_files:
        raise ValueError("No se encontraron archivos JSON en la carpeta de API.")
    
    for json_file in json_files:
        json_file_path = os.path.join(api_folder, json_file)
        process_api_schema_file(json_file_path, avro_output_folder, json_output_folder)
    
    print("Proceso API finalizado. Todos los archivos generados correctamente.")
