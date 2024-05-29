import os
from pathlib import Path
from asyncflows import AsyncFlows


async def main():
    # Find the application and application criteria files
    application_path = os.path.join("application_information", "application.txt")
    application_criteria_path = os.path.join("application_information", "application_criteria.txt")

    # Read the contents of the application and application criteria files
    with open(application_path, "r") as f:
        application = f.read()
    with open(application_criteria_path, "r") as f:
        application_criteria = f.read()

    # Load the application analysis flow
    flow = AsyncFlows.from_file("application_judgement.yaml").set_vars(
        application=application,
        application_criteria=application_criteria,
    )

    # Run the flow and get the result
    result_judge = await flow.run("judgement.result")
    print(result_judge)
    # Optionally run for feedback

    result_suggest = await flow.run("suggestions.result")
    print(result_suggest)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
