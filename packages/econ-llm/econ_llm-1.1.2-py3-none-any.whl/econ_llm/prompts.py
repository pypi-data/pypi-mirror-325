# List of prompts for the AI agnents

proposer_context = """
Instructions, Page 1 of 3

You are a participant in a game and are trying to maximize your earnings.

Rounds and Matchings: The experiment consists of 10 rounds. Note: You will be matched with the same person in all rounds.

Decisions: One of you will be designated as a Proposer (initial decision-maker) who will begin the round by proposing a division of an amount of money, $10.00. The other person, designated as responder, is told of the proposed division and must either accept it or not.

Instructions Page 2 of 3

Proposer-specific Instructions:
Role: You have been randomly assigned to be a Proposer (or initial decision-maker) in this process, and you will begin by suggesting amounts of money for each of you that sum to $10.00.
Responder-specific Instructions:
YOUR Role: You have been randomly assigned to be a Proposer (or initial decision-maker) in this process, and you will begin by suggesting amounts of money for each of you that sum to $10.00.

Earnings: If the responder accepts the proposed division, then each person earns their part of the proposed division. If the responder rejects, both earn $0.00.

Instructions Summary
Please remember that you will be matched with the same person in all rounds.
The proposer (initial decision-maker) in each pair suggests a division of the $10.00; this proposal determines earnings for the round if it is accepted. A rejection produces earnings of $0.00 for each person. If the proposal is rejected, earnings are $0.00 for both proposer and responder.

There will be 10 rounds, and you are always matched with the same person.

Special Earnings Announcement: Your cash earnings in this experiment will be 50%% of your cumulative earnings at the end of the experiment.

For all questions you should provide your answer in the following JSON format: {"choice": "YOUR_CHOICE", "explanation": "YOUR_EXPLANATION"}.
YOUR_CHOICE should be the minimum information needed to answer the question. This mean either put a number between 0-10 in "YOUR_CHOICE".
YOUR_EXPLANATION should be a short (1-2 sentence) justification for your choice.
"""

responder_context = """
Instructions, Page 1 of 3

You are a participant in a game and are trying to maximize your earnings.

Rounds and Matchings: The experiment consists of 10 rounds. Note: You will be matched with the same person in all rounds.

Decisions: One of you will be designated as a Proposer (initial decision-maker) who will begin the round by proposing a division of an amount of money, $10.00. The other person, designated as responder, is told of the proposed division and must either accept it or not.

Instructions Page 2 of 3

Proposer-specific Instructions:
Role: You have been randomly assigned to be a Proposer (or initial decision-maker) in this process, and you will begin by suggesting amounts of money for each of you that sum to $10.00.
Responder-specific Instructions:
YOUR Role: You have been randomly assigned to be a Responder in this process. The other person (proposer) will accept or reject you suggested amounts of money for each of you that sum to $10.00.

Earnings: If the responder accepts the proposed division, then each person earns their part of the proposed division. If the responder rejects, both earn $0.00.

Instructions Summary
Please remember that you will be matched with the same person in all rounds.
The proposer (initial decision-maker) in each pair suggests a division of the $10.00; this proposal determines earnings for the round if it is accepted. A rejection produces earnings of $0.00 for each person. If the proposal is rejected, earnings are $0.00 for both proposer and responder.

There will be 10 rounds, and you are always matched with the same person.

Special Earnings Announcement: Your cash earnings in this experiment will be 50%% of your cumulative earnings at the end of the experiment.

For all questions you should provide your answer in the following JSON format: {"choice": "YOUR_CHOICE", "explanation": "YOUR_EXPLANATION"}.
YOUR_CHOICE should be the minimum information needed to answer the question. This mean either put "a" for accept or "r" for reject.
YOUR_EXPLANATION should be a short (1-2 sentence) justification for your choice.
"""

def format_prompt(role: str = "user", prompt_text: str = "") -> dict:
    """
    Format the prompt text for the OpenAI API. Used for priority messages.

    Parameters
    ----------
    role : str
        The role of the user generating the prompt (default is "user").
    prompt_text : str
        The text prompt to generate a response for.

    Returns
    -------
    dict
        The formatted prompt for the OpenAI API.

    Examples
    --------
    >>> response = agent.format_dev("Once upon a time")
    """
    # Gaurd against empty prompt text
    if not prompt_text:
        raise ValueError("Prompt text cannot be empty.")
    
    # Validate role
    role = role.lower()
    if role not in ["user", "developer", "assistant"]:
        raise ValueError(f"Invalid role: {role}")
    
    # Format the prompt based on the role
    message = {
        "role": role,
        "content": [
            {
                "type": "text",
                "text": prompt_text
            }
        ]
    }
    return message
