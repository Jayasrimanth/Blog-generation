import cohere

COHERE_API_KEY = "RM9pv5Btht8ywtuA37PEORokQ0n7E7G79eVrWdhD"  # Replace with your actual API key
co = cohere.Client(COHERE_API_KEY)

def getCohereResponse(input_text, no_words, blog_style):
    """
    Generate a blog using the Cohere language model.

    Args:
        input_text (str): Topic of the blog.
        no_words (str): Number of words in the blog.
        blog_style (str): Writing style for the blog.

    Returns:
        str: Generated blog content.
    """
    # Prompt Template
    template = f"""
        Write a blog for a {blog_style} job profile on the topic "{input_text}" 
        in approximately {no_words} words.
    """

    # Use Cohere's `generate` endpoint
    response = co.generate(
        model="command-xlarge-nightly",  # Choose an appropriate model
        prompt=template,
        max_tokens=int(no_words) * 4,  # Estimate tokens from word count
        temperature=0.7,  # Control creativity
    )

    return response.generations[0].text.strip()
