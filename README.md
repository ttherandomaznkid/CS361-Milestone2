# CS361-Milestone2

  <h1>JSON to TXT Appender</h1>

  <p>This Python script allows users to extract data from a JSON file and append it to a text (.txt) file. It's particularly useful for scenarios where data needs to be stored in a human-readable format for easy access and review.</p>

  <h2>Features</h2>

  <ul>
    <li><strong>JSON Data Extraction:</strong> The script reads JSON data from a specified file path.</li>
    <li><strong>Appending to TXT:</strong> It appends the extracted data to an existing text file or creates a new one if none exists.</li>
    <li><strong>Prevents Duplicate Entries:</strong> Before appending, it checks for duplicates to avoid redundant data entries.</li>
    <li><strong>User Interaction:</strong> The script interacts with the user, prompting for file paths and providing feedback on the process.</li>
    <li><strong>File Handling:</strong> Proper file handling mechanisms are implemented, including error handling and closure of files.</li>
  </ul>

  <h2>How to Use</h2>

  <ol>
    <li><strong>Clone Repository:</strong> Clone this repository to your local machine.</li>
    <li><strong>Navigate to Directory:</strong> Open your terminal or command prompt and navigate to the directory where the script is located.</li>
    <li><strong>Execute Script:</strong> Run the script by executing the command <code>python script_name.py</code>.</li>
    <li><strong>Follow Prompts:</strong> Follow the prompts to input the paths to your JSON file and TXT file.</li>
    <li><strong>Append Data:</strong> Data from the JSON file will be appended to the TXT file.</li>
    <li><strong>Repeat (Optional):</strong> If desired, you can append more data by responding affirmatively to the prompt.</li>
    <li><strong>Close Files (Optional):</strong> Upon completion, you can choose to close the JSON and TXT files.</li>
  </ol>

  <h2>Requirements</h2>

  <ul>
    <li>Python 3.x</li>
    <li>No additional libraries or dependencies required.</li>
  </ul>

<h2>Example Calling</h2>

```
Enter the path to the JSON file: C:\Users\nicholas\Microservice\sample.json
Enter the path to the TXT file: C:\Users\nicholas\Microservice\sample.txt
New data appended successfully.
Do you want to append more data? (y/n): n
Do you want to close the JSON and TXT files? (y/n): y
PS C:\Users\nicholas\Microservice>
```

<h2>UML Chart</h2>
(https://github.com/ttherandomaznkid/CS361-Milestone2/assets/114196264/6eacd537-9c7e-471e-a435-e8ebdfaeb034)


