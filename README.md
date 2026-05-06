# Askhole CLI: Your Sinister Command Hub

This CLI tool, `askhole`, serves as a guided assistant for navigating, setting up, and executing various components of your development environment, particularly within the context of the ShipWrekD OS and its autonomous agent swarms. It's designed to streamline your workflow, making it easier to manage complex projects with simple commands.

## Philosophy

Embodying the 'Sinister Strategy' or 'Left Hand Path,' Askhole aims to empower autonomous power architecture synthesis. It provides a user-friendly interface to interact with sophisticated AI-driven agent swarms and development tools.

## Features

*   **Codebase Assessment:** Quickly scan and identify key project directories and files.
*   **Setup & Initialization:** Simplified installation of Python and Node.js dependencies.
*   **Execution Hub:** Launch core applications and scripts with ease.
*   **Alias Wizard:** Generate convenient command aliases for frequent operations.
*   **Guided Workflow:** Interactive menus make it easy to manage your projects.

## Installation

1.  **Ensure Python 3 and pip are installed:**
    ```bash
    pkg update && pkg upgrade
    pkg install python
    ```
2.  **Clone or copy the `askhole.py` script into the `askhole-cli` directory within your project root.** (This step is typically done by the orchestrator agent.)

## Usage

### Interactive Mode

Navigate to the `askhole-cli` directory and run the script:

```bash
cd askhole-cli
python3 askhole.py
```

Follow the on-screen menu prompts.

### Command-Line Arguments

Alternatively, you can use direct commands:

*   `python3 askhole.py assess` - Assess the codebase.
*   `python3 askhole.py setup` - Run the setup menu.
*   `python3 askhole.py run` - Access the execution hub.
*   `python3 askhole.py alias` - Run the alias wizard to add commands to your `.bashrc`.

### Aliases

After running the alias wizard (`python3 askhole.py alias`) and restarting your Termux session, you can use these shortcuts:

*   `ask`: Launch the main interactive menu for Askhole.
*   `swarm`: Execute `start_swarm.sh`.
*   `dash`: Launch `zeroclaw_dashboard.py`.
*   `afire`: Run `aFiREFLY_agent/firewarden.py`.

*Note: Ensure you are in the project root directory when using these aliases, as they rely on relative paths.* 

## Project Structure

```
/your_project_root/
├── askhole-cli/
│   ├── askhole.py
│   └── README.md
├── zeroclaw_dashboard.py
├── start_swarm.sh
├── requirements.txt
├── package.json
└── ... (other project files)
```

## Contributing

Contributions are welcome. Please follow the established conventions and the 'Sinister Strategy' guiding philosophy.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.# askhole-cli

Navigator for the Vertical AI / ZeroClaw ecosystem.

## Usage
    python3 askhole.py [assess|services|start|greenroom]

## Commands
    assess      Scan for core files and confirm they exist
    services    Check which processes are live vs dead
    start       Fire dead services (ws_server, listener, Higgins bot)
    greenroom   Write GREENROOM_HANDOFF.md for session handoff

## Alias
    echo "alias askhole='python3 /storage/ED7B-AD5A/root_2026/askhole-cli/askhole.py'" >> ~/.bashrc

## Stack it knows about
    ws_server, AutoDNA, Pancho, Codemate, Higgins Bot,
    Listener, Mrs Higgins, ZeroClaw DB, Boardroom HTML,
    Meatboard, GREENROOM
