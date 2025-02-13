import argparse
import logging
import time
from qubicon.core import QubiconCore, AuthenticatedClient
from rich.console import Console, Group
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from rich.layout import Layout
from rich import print, box
from tabulate import tabulate
from datetime import datetime
from qubicon.api.types import UNSET
import json
from rich.prompt import Confirm
import pandas as pd

# Initialize a Rich console for improved output formatting
console = Console()

# Configure logging to output to both file and console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("qubicon_client.log"),
        logging.StreamHandler(),
    ],
)

# Constants for server options
SERVER_OPTIONS = {
    "1": "https://master.qub-lab.io/",
    "2": "https://release-3.5.qub-lab.io",
}

# Globals for maintaining the client and core state
client = None
qubicon_core = None

def choose_server() -> str:
    """Prompt the user to select a server or provide a custom URL."""
    console.print("[cyan]Choose a server to connect to:[/cyan]")
    console.print("1. ", SERVER_OPTIONS["1"])
    console.print("2. ", SERVER_OPTIONS["2"])
    choice = Prompt.ask("Enter 1, 2, or a custom URL", default="1")
    return SERVER_OPTIONS.get(choice, choice)

def setup_client(base_url: str, token: str):
    """Initialize the authenticated client and core logic."""
    global client, qubicon_core
    client = AuthenticatedClient(base_url=base_url, token=token)
    qubicon_core = QubiconCore(client)

def handle_login():
    """Handle user login and set up the client."""
    base_url = choose_server()
    username = Prompt.ask("Username")
    password = Prompt.ask("Password")

    console.print("[cyan]Attempting to log in...[/cyan]")
    global qubicon_core
    temp_client = AuthenticatedClient(base_url=base_url, token=None)
    temp_core = QubiconCore(temp_client)

    try:
        token = temp_core.login_user(username, password)
        if token:
            console.print("[green]Login successful![/green]")
            setup_client(base_url, token)
        else:
            console.print("[red]Login failed. Check your credentials and try again.[/red]")
    except Exception as e:
        console.print(f"[red]Login error: {e}[/red]")

def handle_login_testing():
    """Handle user login and set up the client."""
    base_url = "https://master.qub-lab.io/"
    username = "qubiconClient"
    password = "qubiconClient1!"

    console.print("[cyan]Attempting to log in...[/cyan]")
    temp_client = AuthenticatedClient(base_url=base_url, token=None)
    temp_core = QubiconCore(temp_client)

    try:
        token = temp_core.login_user(username, password)
        if token:
            console.print("[green]Login successful![/green]")
            setup_client(base_url, token)
        else:
            console.print("[red]Login failed. Check your credentials and try again.[/red]")
    except Exception as e:
        console.print(f"[red]Login error: {e}[/red]")

def ensure_logged_in():
    """Verify that the user is logged in before performing actions."""
    global client, qubicon_core
    if not client or not qubicon_core:
        console.print("[yellow]You are not logged in. Please log in first.[/yellow]")
        handle_login()

def display_menu():
    """Show a compact yet visually appealing menu."""
    menu_table = Table(
        box=box.ROUNDED,
        show_header=False,
        padding=(0, 1),
        min_width=60,
        border_style="bright_black"
    )
    menu_table.add_column("Option", justify="right", width=10, style="bold cyan")
    menu_table.add_column("Action", justify="left", style="dim")
    menu_table.title = "Qubicon CLI Menu"

    # Authentication
    menu_table.add_row("[bold]0[/]", "[white]Login[/]")
    menu_table.add_row("1", "Logout")
    menu_table.add_row("2", "Exit")

    # Models
    menu_table.add_row("[dim] Models ───[/]", "", style="bright_white")
    menu_table.add_row("3", "List models")
    menu_table.add_row("4", "View model details")
    menu_table.add_row("5", "Create model")
    menu_table.add_row("6", "Create advanced model")

    # Quantities
    menu_table.add_row("[dim] Quantities ───[/]", "", style="bright_white")
    menu_table.add_row("7", "List physical quantities")
    menu_table.add_row("8", "Create physical quantity")

    # Processes
    menu_table.add_row("[dim] Processes ───[/]", "", style="bright_white")
    menu_table.add_row("9", "List processes")
    menu_table.add_row("10", "Create process (from recipe)")
    menu_table.add_row("11", "List channels")
    menu_table.add_row("12", "Delete process")

    # Data
    menu_table.add_row("[dim] Data ───[/]", "", style="bright_white")
    menu_table.add_row("13", "Export process data")
    menu_table.add_row("14", "Export model")

    # Recipes & Groups
    menu_table.add_row("[dim] Recipes & Groups ───[/]", "", style="bright_white")
    menu_table.add_row("15", "List recipes")
    menu_table.add_row("16", "View recipe details")
    menu_table.add_row("17", "Create group")
    menu_table.add_row("18", "Add processes to group")

    console.print(menu_table)

def interactive_mode():
    """Interactive loop with improved visual feedback."""
    while True:
        display_menu()
        choice = Prompt.ask(
            "[bold cyan]➤ Select operation[/]",
            choices=[str(i) for i in range(19)],
            show_choices=False
        )

        # Keep existing handler logic
        if choice == "0": handle_login()
        elif choice == "1": handle_logout()
        elif choice == "2":
            console.print("[bold green]Exiting. Goodbye![/]")
            break
        elif choice == "3": display_models()
        elif choice == "4": fetch_model_details()
        elif choice == "5": handle_create_computable_model()
        elif choice == "6": handle_create_advanced_model()
        elif choice == "7": list_physical_quantities()
        elif choice == "8": pass  # create_physical_quantity()
        elif choice == "9": list_processes()
        elif choice == "10": handle_create_process()
        elif choice == "11": fetch_process_channels()
        elif choice == "12": handle_delete_process()
        elif choice == "13": handle_process_data_extraction()
        elif choice == "14": export_model_in_importable_format()
        elif choice == "15": handle_list_recipes()
        elif choice == "16": handle_get_recipe()
        elif choice == "17": handle_create_process_group()
        elif choice == "18": handle_add_processes_to_group()
        else: console.print("[red]Invalid choice. Try again.[/]") 

def handle_delete_process():
    """CLI flow for deleting a process."""
    global qubicon_core
    if not qubicon_core:
        console.print("[red]Error: You must be logged in before deleting a process.[/red]")
        return

    process_id = IntPrompt.ask("Enter the process ID to delete")
    console.print(f"[cyan]Deleting process {process_id}...[/cyan]")
    result = qubicon_core.delete_process(process_id)
    if "success" in result:
        console.print(f"[green]Process {process_id} deleted successfully![/green]")
    else:
        console.print("[red]Failed to delete process.[/red]")

def handle_list_recipes():
    """CLI flow for listing recipes."""
    global qubicon_core
    if not qubicon_core:
        console.print("[red]Error: You must be logged in before listing recipes.[/red]")
        return

    page = IntPrompt.ask("Page (default=0)", default=0)
    size = IntPrompt.ask("Page size (default=400)", default=400)
    recipe_type = Prompt.ask("Recipe type (default=NORMAL)", default="NORMAL")
    statuses_str = Prompt.ask("Statuses (comma-separated, default='DRAFT,RELEASED,GMP')", default="DRAFT,RELEASED,GMP")
    statuses = [s.strip() for s in statuses_str.split(",")]
    sort_str = Prompt.ask("Sort fields (comma-separated, default='updateDate,desc')", default="updateDate,desc")
    sort = [s.strip() for s in sort_str.split(",")]
    search = Prompt.ask("Search string (default='')", default="")

    console.print("[cyan]Listing recipes...[/cyan]")
    result = qubicon_core.list_recipes(
        page=page,
        size=size,
        type=recipe_type,
        statuses=statuses,
        sort=sort,
        search=search,
    )
    if result is None:
        console.print("[red]Failed to list recipes.[/red]")
    else:
        console.print("[green]Recipes:[/green]")
        console.print(result)

def handle_get_recipe():
    """CLI flow for retrieving a single recipe by ID."""
    global qubicon_core
    if not qubicon_core:
        console.print("[red]Error: You must be logged in before getting a recipe.[/red]")
        return

    recipe_id = IntPrompt.ask("Enter the recipe ID")
    console.print(f"[cyan]Fetching recipe {recipe_id}...[/cyan]")
    recipe = qubicon_core.get_recipe(recipe_id)
    if recipe is None:
        console.print("[red]Failed to fetch recipe details.[/red]")
    else:
        console.print("[green]Recipe details:[/green]")
        console.print(recipe)

def handle_create_process_group():
    """CLI flow for creating a new process group."""
    global qubicon_core
    if not qubicon_core:
        console.print("[red]Error: You must be logged in before creating a process group.[/red]")
        return

    group_name = Prompt.ask("Enter a name for the new process group")

    console.print(f"[cyan]Creating process group '{group_name}'...[/cyan]")
    try:
        group = qubicon_core.create_process_group(name=group_name)
        if group:
            console.print("[green]Process group created successfully![/green]")
            console.print(group)
        else:
            console.print("[red]Failed to create process group.[/red]")
    except Exception as e:
        console.print(f"[red]Error creating process group: {e}[/red]")

def handle_add_processes_to_group():
    """CLI flow for adding processes to an existing group."""
    global qubicon_core
    if not qubicon_core:
        console.print("[red]Error: You must be logged in before modifying a process group.[/red]")
        return

    group_id = IntPrompt.ask("Enter the group ID")
    console.print("Enter process IDs to add to group, comma-separated.")
    pids_str = Prompt.ask("Process IDs")
    try:
        process_ids = [int(pid.strip()) for pid in pids_str.split(",")]
    except ValueError:
        console.print("[red]Invalid input. Please enter numeric IDs, comma-separated.[/red]")
        return

    console.print(f"[cyan]Adding processes {process_ids} to group {group_id}...[/cyan]")
    try:
        updated_group = qubicon_core.add_processes_to_group(group_id, process_ids)
        if updated_group:
            console.print("[green]Processes added successfully![/green]")
            console.print(updated_group)
        else:
            console.print("[red]Failed to update process group.[/red]")
    except Exception as e:
        console.print(f"[red]Error updating process group: {e}[/red]")

def handle_create_process():
    """CLI flow for creating a new process from a chosen recipe."""
    global qubicon_core

    if not qubicon_core:
        console.print("[red]Error: You must be logged in before creating a process.[/red]")
        return

    # Ask the user for process details
    process_name = Prompt.ask("Enter a name for the new process")
    recipe_id = IntPrompt.ask("Enter the recipe ID to base this process on")

    # Optional: ask for description, or skip if not needed
    description = Prompt.ask("Enter process description (optional)", default="")

    # Create the process via QubiconCore
    console.print(f"[cyan]Creating process '{process_name}' using recipe ID {recipe_id}...[/cyan]")
    try:
        result = qubicon_core.create_process(
            name=process_name,
            recipe_id=recipe_id,
            description=description,
            # add other optional args if desired: online_equipment_ids, offline_equipment_ids, etc.
        )
        if result:
            console.print(f"[green]Process created successfully![/green]\n{result}")
        else:
            console.print("[red]Failed to create process.[/red]")
    except Exception as e:
        console.print(f"[red]Error creating process: {e}[/red]")

def fetch_process_channels():
    """Fetch and display channels for a specific process."""
    process_id = Prompt.ask("Enter the Process ID", default="0")
    process_phase_id = Prompt.ask("Enter Process Phase ID (or leave blank)", default=UNSET)
    channel_name = Prompt.ask("Enter Channel Name (or leave blank)", default=UNSET)
    node_types_input = Prompt.ask("Enter Node Types (comma-separated, e.g., INPUT,OUTPUT) or leave blank", default=UNSET)
    sensor_type_ids_input = Prompt.ask("Enter Sensor Type IDs (comma-separated, e.g., 1,2,3) or leave blank", default=UNSET)
    physical_quantity_unit_id = Prompt.ask("Enter Physical Quantity Unit ID (or leave blank)", default=UNSET)

    ensure_logged_in()

    try:
        # Prepare the keyword arguments dynamically
        kwargs = {"process_id": int(process_id)}

        # Add filters to kwargs only if they are not UNSET
        if process_phase_id is not UNSET:
            kwargs["process_phase_id"] = int(process_phase_id)
        if channel_name is not UNSET:
            kwargs["name"] = channel_name
        if node_types_input is not UNSET:
            kwargs["node_types"] = [x.strip() for x in node_types_input.split(",") if x.strip()]
        if sensor_type_ids_input is not UNSET:
            kwargs["sensor_type_ids"] = [int(x.strip()) for x in sensor_type_ids_input.split(",") if x.strip()]
        if physical_quantity_unit_id is not UNSET:
            kwargs["physical_quantity_unit_id"] = int(physical_quantity_unit_id)

        # Fetch channels using the core function
        channels = qubicon_core.extract_channels(**kwargs)

        # Check if the response contains channels
        if isinstance(channels, dict) and "content" in channels:
            # Display the channels in a table
            table = Table(title=f"Channels for Process {process_id}", expand=True)
            table.add_column("ID", justify="right", style="cyan")
            table.add_column("Name", justify="left", style="magenta")
            table.add_column("Node Type", justify="left", style="green")
            table.add_column("Unit", justify="left", style="blue")
            table.add_column("Physical Quantity", justify="left", style="yellow")
            table.add_column("Equipment Name", justify="left", style="white")

            for channel in channels["content"]:
                physical_quantity = channel.get("physicalQuantityUnit", {})
                table.add_row(
                    str(channel.get("id", "N/A")),
                    channel.get("name", "N/A"),
                    channel.get("nodeType", "N/A"),
                    physical_quantity.get("unit", "N/A"),
                    physical_quantity.get("name", "N/A"),
                    channel.get("equipmentName", "N/A"),
                )

            console.print(table)

        elif isinstance(channels, dict) and "error" in channels:
            console.print(f"[red]Error: {channels['error']}[/red]")
        else:
            console.print("[yellow]No channels found for the given process ID.[/yellow]")

    except Exception as e:
        console.print(f"[red]Error fetching process channels: {e}[/red]")

def display_models():
    """Fetch and display all computable models in a structured table format."""
    ensure_logged_in()
    try:
        # Fetch the models from the core function
        response = qubicon_core.list_computable_models()

        if "content" in response and isinstance(response["content"], list):
            # Create a Rich table for formatted output
            table = Table(title="Computable Models", expand=True)
            table.add_column("ID", justify="center", style="cyan", no_wrap=True)
            table.add_column("KPI Name", justify="center", style="magenta", no_wrap=True)
            table.add_column("Status", justify="center", style="green", no_wrap=True)
            table.add_column("Calculation Style", justify="center", style="yellow", no_wrap=True)
            table.add_column("Engine Type", justify="center", style="red", no_wrap=True)
            table.add_column("Update Date", justify="center", style="white", no_wrap=True)
            table.add_column("Creation Date", justify="center", style="white", no_wrap=True)

            # Add rows to the table
            for model in response["content"]:
                table.add_row(
                    str(model.get("id", "N/A")),
                    model.get("kpiName", "N/A"),
                    model.get("status", "N/A"),
                    model.get("calculationStyle", "N/A"),
                    model.get("engineType", "N/A"),
                    str(model.get("updateDate", "N/A")),
                    str(model.get("creationDate", "N/A")),
                )

            # Print the table
            console.print(table)
        else:
            console.print("[yellow]No models found or unexpected response format.[/yellow]")

    except Exception as e:
        console.print(f"[red]Error listing models: {e}[/red]")

def fetch_model_details():
    """Fetch and display details for a specific model."""
    model_id = Prompt.ask("Enter the model ID", default="0")
    ensure_logged_in()
    try:
        details = qubicon_core.fetch_model_details(int(model_id))
        if details:
            table = Table(title="Model Details", expand=True)
            table.add_column("Property", justify="right", style="cyan")
            table.add_column("Value", justify="left", style="magenta")

            for key, value in sorted(details.items()):
                # Format nested JSON-like objects
                if isinstance(value, (list, dict)):
                    formatted_value = json.dumps(value, indent=4, ensure_ascii=False)
                    table.add_row(str(key), formatted_value)
                else:
                    table.add_row(str(key), str(value))
            
            console.print(table)
        else:
            console.print("[red]No details found for the specified model.[/red]")
    except Exception as e:
        console.print(f"[red]Error fetching model details: {e}[/red]")

def list_physical_quantities():
    """Fetch and display all physical quantities with their units."""
    ensure_logged_in()
    try:
        # Fetch the physical quantities from the core function
        quantities = qubicon_core.list_physical_quantities()
        if quantities:
            # Create a Rich table for formatted output
            table = Table(title="Physical Quantities", expand=True)
            table.add_column("ID", justify="right", style="cyan")
            table.add_column("Name", justify="left", style="magenta")
            table.add_column("Units", justify="left", style="green")

            # Add rows to the table
            for quantity in sorted(quantities, key=lambda x: x['id']):
                # Extract units and format as a comma-separated list
                units = (
                    ", ".join(unit.get("unit", "N/A") for unit in quantity.get("units", []))
                    if "units" in quantity and isinstance(quantity["units"], list)
                    else "N/A"
                )
                table.add_row(
                    str(quantity["id"]),
                    quantity.get("name", "N/A"),
                    units,
                )

            # Print the table
            console.print(table)
        else:
            console.print("[red]No physical quantities found.[/red]")
    except Exception as e:
        console.print(f"[red]Error listing physical quantities: {e}[/red]")

def list_processes():
    """Fetch and display all processes."""
    ensure_logged_in()
    try:
        # Fetch the processes from the core function
        response = qubicon_core.list_processes()

        if "content" in response and isinstance(response["content"], list):
            processes = response["content"]

            if processes:
                # Create a table for displaying processes
                table = Table(title="Processes", expand=True)
                table.add_column("ID", justify="right", style="cyan")
                table.add_column("Name", justify="left", style="magenta")
                table.add_column("Description", justify="left", style="green")
                table.add_column("Status", justify="left", style="yellow")
                table.add_column("Type", justify="left", style="blue")
                table.add_column("Creation Date", justify="left", style="white")
                table.add_column("End Date", justify="left", style="white")

                for process in sorted(processes, key=lambda x: x['id']):
                    # Format dates from Unix timestamps
                    creation_date = process.get('creationDate', None)
                    end_date = process.get('endDate', None)
                    formatted_creation_date = (
                        datetime.utcfromtimestamp(creation_date / 1000).strftime('%Y-%m-%d %H:%M:%S')
                        if creation_date else "N/A"
                    )
                    formatted_end_date = (
                        datetime.utcfromtimestamp(end_date / 1000).strftime('%Y-%m-%d %H:%M:%S')
                        if end_date else "N/A"
                    )

                    # Add rows to the table
                    table.add_row(
                        str(process['id']),
                        process.get('name', 'N/A'),
                        process.get('description', 'N/A'),
                        process.get('status', 'N/A'),
                        process.get('type', 'N/A'),
                        formatted_creation_date,
                        formatted_end_date
                    )

                console.print(table)
            else:
                console.print("[yellow]No processes found.[/yellow]")
        elif "error" in response:
            console.print(f"[red]{response['error']}[/red]")
        else:
            console.print("[yellow]Unexpected response format.[/yellow]")

    except Exception as e:
        console.print(f"[red]Error listing processes: {e}[/red]")

def handle_process_data_extraction():
    """Interactive process data extraction."""
    ensure_logged_in()
    try:
        # Prompt for Process ID and validate it
        process_id = int(Prompt.ask("Enter the Process ID to extract data from", default="1"))

        # Fetch the start and end time for the process
        start_time = int(Prompt.ask("Enter the start time (Unix timestamp in ms)", default="0"))
        end_time = int(Prompt.ask("Enter the end time (Unix timestamp in ms)", default="0"))

        # Optional parameters for data extraction
        raw_mode = Confirm.ask("Enable raw mode?", default=False)
        export_rate = int(Prompt.ask("Enter the export rate (granularity in ms)", default="148"))
        at_sampling_timestamps_mode = Confirm.ask("Export at sampling timestamps?", default=False)
        included_report = Confirm.ask("Include report in export?", default=False)

        # Prompt for optional event IDs
        start_event_id_input = Prompt.ask("Enter start event ID (or leave blank)", default="")
        end_event_id_input = Prompt.ask("Enter end event ID (or leave blank)", default="")
        start_event_id = int(start_event_id_input) if start_event_id_input else UNSET
        end_event_id = int(end_event_id_input) if end_event_id_input else UNSET

        # Output format selection
        output_format = Prompt.ask("Enter your format of choice (csv or json)", choices=["csv", "json"], default="csv")
        output_file = Prompt.ask("Enter the output file path", default="process_data.csv" if output_format == "csv" else "process_data.json")

        # Extract process data using the core function
        response = qubicon_core.extract_process_data(
            process_id=process_id,
            start_time=start_time,
            end_time=end_time,
            raw_mode=raw_mode,
            export_rate=export_rate,
            at_sampling_timestamps_mode=at_sampling_timestamps_mode,
            included_report=included_report,
            start_event_id=start_event_id,
            end_event_id=end_event_id,
        )

        # Handle the response and save the output
        if "error" not in response:
            if output_format == "csv":
                # Convert JSON data to CSV and save
                df = pd.DataFrame(response["data"])  # Adjust based on the response structure
                df.to_csv(output_file, index=False)
                console.print(f"[green]Process data successfully saved to {output_file} in CSV format.[/green]")
            else:
                # Save as JSON
                with open(output_file, "w") as f:
                    json.dump(response, f, indent=4)
                console.print(f"[green]Process data successfully saved to {output_file} in JSON format.[/green]")
        else:
            console.print(f"[red]Error: {response['error']}[/red]")

    except Exception as e:
        console.print(f"[red]Unexpected error: {str(e)}[/red]")

def handle_logout():
    """Log out the user and clear session data."""
    global client, qubicon_core
    client = None
    qubicon_core = None
    console.print("[green]Logged out successfully.[/green]")

def export_model_in_importable_format():
    """Extract a model in a format that can be imported."""
    ensure_logged_in()
    model_id = Prompt.ask("Enter the model ID", default="0")
    output_file = Prompt.ask("Enter the output file path", default="exported_model.json")
    try:
        response = qubicon_core.export_model_to_json(int(model_id), output_file)
    except Exception as e:
        console.print(f"[red]Error extracting model: {e}[red]")

def handle_create_computable_model():
    """Create a new computable model interactively."""
    ensure_logged_in()
    try:
        model_data = Prompt.ask("Enter the path to the JSON file")
        # turn json file into dict
        with open(model_data) as f:
            model_data = json.load(f)
        print(model_data)
        response = qubicon_core.create_computable_model(model_data)
        
        if response:
            console.print("[green]Model created successfully![green]")
    except Exception as e:
        console.print(f"[red]Error creating model: {e}[red]")

def handle_create_advanced_model():
    """CLI flow for creating an advanced computable model (with external file upload)."""
    ensure_logged_in()
    try:
        # Prompt for the JSON file path containing the advanced model data.
        json_file_path = Prompt.ask("Enter the path to the JSON file containing the advanced model data")
        with open(json_file_path, "r") as f:
            model_data = json.load(f)
        
        # Prompt for the ZIP file path that holds the external model files.
        zip_file_path = Prompt.ask("Enter the path to the ZIP file for the advanced model")
        
        console.print("[cyan]Creating advanced computable model...[/cyan]")
        response = qubicon_core.create_advanced_model(model_data, zip_file_path)
        
        if response:
            console.print("[green]Advanced model created successfully![/green]")
            console.print(response)
        else:
            console.print("[red]Failed to create advanced model.[/red]")
    except Exception as e:
        console.print(f"[red]Error creating advanced model: {e}[/red]")


def main():
    """Entry point for the CLI application."""
    parser = argparse.ArgumentParser(description="Qubicon API Interactive Client")
    parser.add_argument("--interactive", action="store_true", help="Launch interactive mode")
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    else:
        console.print("[yellow]Use --interactive to start the CLI.[/yellow]")

if __name__ == "__main__":
    main()
