from agentmake import PACKAGE_PATH, config, generate, load_configurations
from agentmake.utils.handle_text import readTextFile, writeTextFile
import argparse, os, pprint

def chat():
    main(keep_chat_record=True)

def main(keep_chat_record=False):
    # Create the parser
    parser = argparse.ArgumentParser(description = """ToolMate AI API client `tm` cli options""")
    # Add arguments for running `generate` function
    parser.add_argument("default", nargs="*", default=None, help="prompt")
    parser.add_argument("-b", "--backend", action="store", dest="backend", help="AI backend")
    parser.add_argument("-m", "--model", action="store", dest="model", help="AI model")
    parser.add_argument("-mka", "--model_keep_alive", action="store", dest="model_keep_alive", help="time to keep the model loaded in memory; applicable to ollama only")
    parser.add_argument("-sys", "--system", action='append', dest="system", help="system message")
    parser.add_argument("-con", "--context", action='append', dest="context", help="predefined context that is added as the user prompt prefix")
    parser.add_argument("-fup", "--follow_up_prompt", action='append', dest="follow_up_prompt", help="follow-up prompts after an assistant message is generated")
    parser.add_argument("-icp", "--input_content_plugin", action='append', dest="input_content_plugin", help="plugin(s) that works on user input")
    parser.add_argument("-ocp", "--output_content_plugin", action='append', dest="output_content_plugin", help="plugin(s) that works on assistant response")
    parser.add_argument("-a", "--agent", action='append', dest="agent", help="agentmake-compatible agent(s)")
    parser.add_argument("-t", "--tool", action='append', dest="tool", help="agentmake-compatible tool(s)")
    parser.add_argument("-s", "--schema", action='store', dest="schema", help="json schema for structured output")
    parser.add_argument("-tem", "--temperature", action='store', dest="temperature", type=float, help="temperature for sampling")
    parser.add_argument("-mt", "--max_tokens", action='store', dest="max_tokens", type=int, help="maximum number of tokens to generate")
    parser.add_argument("-cw", "--context_window", action='store', dest="context_window", type=int, help="context window size; applicable to ollama only")
    parser.add_argument("-bs", "--batch_size", action='store', dest="batch_size", type=int, help="batch size; applicable to ollama only")
    parser.add_argument("-pre", "--prefill", action='append', dest="prefill", help="prefill of assistant message; applicable to deepseek, mistral, ollama and groq only")
    parser.add_argument("-sto", "--stop", action='append', dest="stop", help="stop sequences")
    parser.add_argument("-key", "--api_key", action="store", dest="api_key", help="API key")
    parser.add_argument("-end", "--api_endpoint", action="store", dest="api_endpoint", help="API endpoint")
    parser.add_argument("-pi", "--api_project_id", action="store", dest="api_project_id", help="project id; applicable to Vertex AI only")
    parser.add_argument("-sl", "--api_service_location", action="store", dest="api_service_location", help="cloud service location; applicable to Vertex AI only")
    parser.add_argument("-tim", "--api_timeout", action="store", dest="api_timeout", type=float, help="timeout for API request")
    parser.add_argument("-ww", "--word_wrap", action="store_true", dest="word_wrap", help="wrap output text according to current terminal width")
    # others
    parser.add_argument("-c", "--chat", action="store_true", dest="chat", help="enable chat feature")
    parser.add_argument("-cf", "--chat_file", action="store", dest="chat_file", help="load the conversation recorded in the given file")
    parser.add_argument("-n", "--new_conversation", action="store_true", dest="new_conversation", help="new conversation; applicable when chat feature is enabled")
    parser.add_argument("-e", "--export_conversation", action="store", dest="export_conversation", help="export conversation to a chat file; specify the file path for the export; applicable when chat feature is enabled")
    parser.add_argument("-lc", "--load_configurations", action="store", dest="load_configurations", help="load the environment variables specified in the given file")
    # Parse arguments
    args = parser.parse_args()

    # load configurations
    if args.load_configurations and os.path.isfile(args.load_configurations):
        load_configurations(args.load_configurations)

    user_prompt = " ".join(args.default) if args.default is not None else ""
    follow_up_prompt = args.follow_up_prompt if args.follow_up_prompt else []
    if args.chat:
        keep_chat_record = True
    if keep_chat_record:
        if args.new_conversation:
            config.messages = []
        elif args.chat_file:
            if os.path.isfile(args.chat_file):
                try:
                    content = "config.messages = " + readTextFile(args.chat_file)
                    exec(content, globals())
                except:
                    raise ValueError("Error! Chat file format is invalid!")
            else:
                raise ValueError("Error! Given chat file path does not exist!")
    if keep_chat_record and config.messages:
        follow_up_prompt.insert(0, user_prompt)

    # run generate function
    generated_messages = generate(
        messages=config.messages if keep_chat_record and config.messages else user_prompt,
        backend=args.backend,
        model=args.model,
        model_keep_alive=args.model_keep_alive,
        system=args.system,
        context=args.context,
        follow_up_prompt=follow_up_prompt,
        input_content_plugin=args.input_content_plugin,
        output_content_plugin=args.output_content_plugin,
        agent=args.agent,
        tool=args.tool,
        schema=args.schema,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        context_window=args.context_window,
        batch_size=args.batch_size,
        prefill=args.prefill,
        stop=args.stop,
        api_key=args.api_key,
        api_endpoint=args.api_endpoint,
        api_project_id=args.api_project_id,
        api_service_location=args.api_service_location,
        api_timeout=int(args.api_timeout) if args.api_timeout and args.backend and args.backend in ("cohere", "mistral") else args.api_timeout,
        word_wrap=args.word_wrap,
    )
    if keep_chat_record:
        config_file = os.path.join(PACKAGE_PATH, "config.py")
        config_content = "messages = " + pprint.pformat(generated_messages)
        writeTextFile(config_file, config_content)
        if args.export_conversation:
            try:
                writeTextFile(args.export_conversation, pprint.pformat(generated_messages))
            except:
                raise ValueError(f"Error! Failed to export conversation to '{args.export_conversation}'!")

if __name__ == "__main__":
    test = main()
