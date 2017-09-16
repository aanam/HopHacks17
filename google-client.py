from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six

def entities_text(text):
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
        # Instantiates a plain text document.
        document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

        # Detects entities in the document. You can also analyze HTML with:
        #   document.type == enums.Document.Type.HTML
        entities = client.analyze_entities(document).entities

        # entity types from enums.Entity.Type
        entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION', 'EVENT', 'DISASTER', 'CALAMITY', 'CRISIS', 'Hurricane', 'Flood', 'Earthquake')

        for entity in entities:
            print('=' * 20)
            print(u'{:<16}: {}'.format('name', entity.name))
            print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
            print(u'{:<16}: {}'.format('metadata', entity.metadata))
            print(u'{:<16}: {}'.format('salience', entity.salience))
            print(u'{:<16}: {}'.format('wikipedia_url',
            entity.metadata.get('wikipedia_url', '-')))


if __name__ == "__main__":
    txt= "Hello there, I'm ananth from UMBC"
    txt = "hurricane Irma has destroyed Florida"
    entities_text(txt)

