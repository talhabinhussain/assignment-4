from agents import Agent,Runner,RunConfig,AsyncOpenAI,OpenAIChatCompletionsModel,function_tool
from dotenv import load_dotenv,find_dotenv
import os
from tools.weather_api import get_weather

load_dotenv(find_dotenv(),override=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("BASE_URL")
gemini_ai_model = os.getenv("AI_MODEL")


external_client = AsyncOpenAI(api_key=gemini_api_key,base_url=gemini_base_url)

Model = OpenAIChatCompletionsModel(openai_client=external_client,model=gemini_ai_model)



weather_agent = Agent(
    name="Weather Agent",
    instructions="You are weather agent simple call the tool and give output to the user and make output user freindly that user understand the temperature weather and humidity percent  ",
    tools=[get_weather]
)
config = RunConfig(model=Model,model_provider=external_client,tracing_disabled=True)
prompt = input("Enter Your Question ")
result = Runner.run_sync(weather_agent,prompt,run_config=config)

print(result.final_output)