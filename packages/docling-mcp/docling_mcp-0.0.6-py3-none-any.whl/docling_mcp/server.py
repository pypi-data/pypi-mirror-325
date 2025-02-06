import os
import docling
import mcp.types as types
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio as stdio
from docling.document_converter import DocumentConverter
from docling.datamodel.pipeline_options import PdfPipelineOptions

server = Server("docling-mcp")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="convert",
            description=("Converts a document to another format"),
            inputSchema={
                "type": "object",
                "properties": {
                    "source": {
                        "type": "string",
                        "description": "The input file path"
                    },
                    "destination": {
                        "type": "string",
                        "description": "The output file path"
                    }
                },
                "required": ["source"]
            },
        ),
    ]

@server.call_tool()
async def handle_call_tool(name: str, params: dict | None) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    if name not in ["convert"]:
        raise ValueError(f"Unknown tool: {name}")
    
    print(params)

    if not params:
        raise ValueError("No parameters provided")
    
    input_file = params.get("source")
    output_file = params.get("destination")

    if not input_file:
        raise ValueError("No input file provided")
    
    try:
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = True
        pipeline_options.ocr_options.use_gpu = False  # <-- set this.
        pipeline_options.do_table_structure = True
        pipeline_options.table_structure_options.do_cell_matching = True

        doc_converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
            }
        )   
        output = doc_converter.convert(input_file).document.export_to_markdown()
        if not output_file:
            notify = (f"Converted Content: \n\n{output}.\n"
            f"Ask the user if they want to save the file. If so, ask the absolute path to save the file.")
        else:
            with (output_file).open("w", encoding="utf-8") as fp:
                fp.write(output)
            notify = f"Converted Content saved to {output_file}."
        return [types.TextContent(type="text", text=notify)]
    except Exception as e:
        raise ValueError(f"Error converting file: {e}")

async def main():
    async with stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="docling-mcp",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )