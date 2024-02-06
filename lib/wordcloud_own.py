import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords

def generate_wordcloud(text, save_path=None):
    """
    Generates and displays a word cloud from the provided text.
    Optionally saves the word cloud image to a specified path.

    :param text: String of text from which to generate the word cloud.
    :param save_path: Optional; Path to save the word cloud image.
    """
    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=set(stopwords.words('english')),
                          min_font_size=10).generate(text)

    # Plot the WordCloud image                        
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    # Save the word cloud image if a path is provided
    if save_path:
        plt.savefig(save_path)

    plt.show()


if __name__ == "__main__":
    # This block is for testing the function with example text.
    example_text = "Your example text goes here. You can replace this with any text you want to test."
    generate_wordcloud(example_text)
