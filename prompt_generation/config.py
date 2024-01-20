
knowledge = [
        """The network connection is experiencing issues (E101). Users may encounter difficulties when trying to establish a connection with the server or remote resource. This can be attributed to a weak or unstable internet connection, network configuration problems, or server unavailability. To troubleshoot this error, users should ensure that their network settings are configured correctly, verify the stability of their internet connection, and attempt to reconnect. If the problem persists, contacting the internet service provider or network administrator is recommended for further assistance.""",
        """File corruption or missing files (F205) can lead to errors within applications or software. This error occurs when a required file or resource is damaged, deleted, or inaccessible. Such issues may arise from software bugs, improper installations, or disk drive malfunctions. Resolving this error typically involves reinstalling the affected software or application, restoring the missing file from a backup, or running a disk repair utility. If users are unable to resolve the issue independently, it is advisable to seek assistance from the software vendor or technical support.""",
        """Hardware malfunctions or compatibility problems (H312) may cause errors and disruptions in system performance. The error arises from issues related to the hardware components or devices being used. Outdated drivers, incompatible hardware, or faulty connections can be the root cause. Users encountering this error should ensure that all hardware components are properly connected, update drivers to the latest version, and check for compatibility with the operating system. If the error persists, it is recommended to seek assistance from the manufacturer's support team or consult with a qualified technician.""",
        """Insufficient memory allocation (M407) can hinder the execution of specific tasks within a program or application. This error occurs when there is not enough memory available. Common causes of this error include memory leaks, excessive resource usage, or inadequate system memory. To address this issue, users can close unnecessary programs or processes to free up memory, increase the system's virtual memory allocation, or consider upgrading the RAM if necessary. If the problem continues to persist, it is advisable to contact technical support or consult with a computer specialist for further guidance.""",
        """During software updates or installations, users may encounter the P511 error. This error indicates that there was an error while updating or installing a program. Incompatible software versions, insufficient disk space, or interrupted installation processes can lead to this error. To resolve this, users should ensure that they have enough disk space available, temporarily disable any antivirus or firewall software, and restart the installation or update process. If the error persists, it is recommended to reach out to the software vendor or support team for further assistance.""",
        """Security-related issues (S805) can cause authentication or authorization problems, leading to the S805 error. This error may occur due to incorrect login credentials, expired certificates, or permission restrictions. Users encountering this error should double-check their login details, ensure that certificates are up to date, and verify the user's permissions. If the issue persists, it is advisable to contact the system administrator or support team to resolve the security-related concern.""",
        """The T912 error indicates a failure in the transmission of data between devices or applications, often due to communication protocol issues. This error may occur as a result of network disruptions, misconfigured protocols, or incompatible communication settings. To troubleshoot this error, users should check their network connection, ensure that the communication settings match between the devices, and attempt to restart the communication process. If the error persists, contacting the technical support team or referring to the documentation for the specific protocol may be necessary.""",
        """Video playback issues (Error 500) can arise due to various factors, causing difficulties in playing video content. These factors may include unsupported video codecs, incompatible media players, or corrupted video files. Users encountering this error should ensure that they have the necessary video codecs installed, try using a different media player, or attempt to play the video file on another device.""",

        """ Those who consistently averaged less than one cigarette per day over their lifetime had nine times the risk of dying from lung cancer than never smokers. Among people who smoked between one and 10 cigarettes per day, the risk of dying from lung cancer was nearly 12 times higher than that of never smokers.""",
        """A pebble is a clast of rock with a particle size of 4 to 64 millimetres based on the Udden-Wentworth scale of sedimentology. Pebbles are generally considered larger than granules (2 to 4 millimetres diameter) and smaller than cobbles (64 to 256 millimetres diameter).""",
        """Fish are more intelligent than they appear. In many areas, such as memory, their cognitive powers match or exceed those of ’higher’ vertebrates including non-human primates. Fish’s long-term memories help them keep track of complex social relationships.""",
        """Condensation occurs on eyeglass lenses when water vapor from your sweat, breath, and ambient humidity lands on a cold surface, cools, and then changes into tiny drops of liquid, forming a film that you see as fog. Your lenses will be relatively cool compared to your breath, especially when the outside air is cold."""
        """Greece is approximately 131,957 sq km, while Mexico is approximately 1,964,375 sq km, making Mexico 1,389% larger than Greece."""
]

questions = [
        """A common effect of smoking lots of cigarettes in one’s lifetime is a higher than normal chance of getting lung cancer.""",
        """A rock is the same size as a pebble.""",
        """A fish is capable of thinking.""",
        """Glasses always fog up"""
]

PROMPT_TEMPLATE = """You will answer a question given a provided knowledge.\nQuestion: {question}\nKnowledge:{knowledge}"""
EVALUATION_PROMPT_TEMPLATE = """You are an evaluator. I will provide you with a question, knowledge and an answer. I will also provide a question for each of those metrics, and you will return 1 if the answer is positive, 0 if negative, as a score for that metric. Just answer with the name of the metric and the score, nothing else. 

Question:
{question}

Knowledge:
{knowledge}

Answer:
{answer}

Metrics:
- Explicit: Is the question contained explicitly in the answer or has a literal mention to parts or it?
- Helpfulness: Does the provided answer really helps answer and support or contradict the question?
- Directness: Does the provided answer support the question directly?
- Grammaticality: Is the answer gramatically correct and complete?
- Relevance: Is the answer relevant to the question and covers the same topics and no other topics?
- Edge: Does the answer contain edge cases?
- Factuality: Does the answer only provide facts from the knowledge and nothing else?
- Supposition: Does the answer contain a conclusion or supposition extracted by analyzing the knowledge?
- Objectivity: Is the answer provided totally objective given what is expressed in the knowledge?
- Creativity: What is the level of creativity present in the answer given the question?
- ThirdPartyOpinion: Does the answer contain a third-party opinion?
- Source: Does the answer provide the source of information?"""


THRESHOLD = 0.35
LOW_CONFIDENCE = "DISCARDED"
STORE_PATH = "__store__"

positive = ['Explicit', 'Helpfulness', 'Directness', 'Grammaticality', 'Relevance', 'Factuality', 'Objectivity', 'Source']
negative = ['Edge', 'Creativity', 'Supposition', 'ThirdPartyOpinion']