// Create a button element
const submitButton = document.createElement('button');
submitButton.textContent = 'Submit File';
submitButton.style.backgroundColor = 'green';
submitButton.style.color = 'white';
submitButton.style.padding = '5px';
submitButton.style.border = 'none';
submitButton.style.borderRadius = '5px';
submitButton.style.margin = '5px';

// Create a progress element
const progressBar = document.createElement('div');
progressBar.style.width = '99%';
progressBar.style.height = '5px';
progressBar.style.backgroundColor = 'grey';
const progressBarInner = document.createElement('div');
progressBarInner.style.width = '0%';
progressBarInner.style.height = '100%';
progressBarInner.style.backgroundColor = 'blue';
progressBar.appendChild(progressBarInner);

// Find the target element by class name
const targetElement = document.querySelector('.flex.flex-col.w-full.py-2.flex-grow.md\\:py-3.md\\:pl-4');

// Insert the button and progress bar before the target element
targetElement.parentNode.insertBefore(submitButton, targetElement);
targetElement.parentNode.insertBefore(progressBar, targetElement);

// Function to submit conversation
async function submitConversation(text, part, filename) {
  const textarea = document.querySelector("textarea[tabindex='0']");
  const enterKeyEvent = new KeyboardEvent("keydown", {
    bubbles: true,
    cancelable: true,
    keyCode: 13,
  });
  textarea.value = `Part ${part} of ${filename}:\n\n${text}`;
  textarea.dispatchEvent(enterKeyEvent);
}

// Function to check if ChatGPT is ready
async function waitForChatGPT() {
  let chatgptReady = false;
  while (!chatgptReady) {
    await new Promise(resolve => setTimeout(resolve, 1000));
    chatgptReady = !document.querySelector(".text-2xl > span:not(.invisible)");
  }
}

// Add click event listener to the submit button
submitButton.addEventListener('click', async () => {
  const input = document.createElement('input');
  input.type = 'file';
  input.accept = '.txt, .js, .py, .html, .css, .json, .csv';
  input.onchange = async (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = async (e) => {
        const content = e.target.result;
        const chunkSize = 15000;
        const numChunks = Math.ceil(content.length / chunkSize);
        
        for (let i = 0; i < numChunks; i++) {
          const start = i * chunkSize;
          const end = (i + 1) * chunkSize;
          const chunk = content.slice(start, end);
          
          await submitConversation(chunk, i + 1, file.name);
          progressBarInner.style.width = `${((i + 1) / numChunks) * 100}%`;
        }
        
        progressBarInner.style.backgroundColor = 'blue';
        await waitForChatGPT();
      };
      reader.readAsText(file);
    }
  };
  input.click();
});
//-----------------------------------------------------------------------------------------

document.addEventListener('DOMContentLoaded', () => {
    // Create a button element
    const submitButton = document.createElement('button');
    submitButton.textContent = 'Submit File';
    submitButton.style.backgroundColor = 'green';
    submitButton.style.color = 'white';
    submitButton.style.padding = '5px';
    submitButton.style.border = 'none';
    submitButton.style.borderRadius = '5px';
    submitButton.style.margin = '5px';
  
    // Create a progress element
    const progressBar = document.createElement('div');
    progressBar.style.width = '99%';
    progressBar.style.height = '5px';
    progressBar.style.backgroundColor = 'grey';
    const progressBarInner = document.createElement('div');
    progressBarInner.style.width = '0%';
    progressBarInner.style.height = '100%';
    progressBarInner.style.backgroundColor = 'blue';
    progressBar.appendChild(progressBarInner);
  
    // Find the target element by class name
    const targetElement = document.querySelector('.flex.flex-col.w-full.py-2.flex-grow.md\\:py-3.md\\:pl-4');
  
    if (targetElement) {
      // Insert the button and progress bar before the target element
      targetElement.parentNode.insertBefore(submitButton, targetElement);
      targetElement.parentNode.insertBefore(progressBar, targetElement);
  
      // Rest of your code goes here...
  
      // Function to submit conversation
      async function submitConversation(text, part, filename) {
        const textarea = document.querySelector("textarea[tabindex='0']");
        const enterKeyEvent = new KeyboardEvent("keydown", {
          bubbles: true,
          cancelable: true,
          keyCode: 13,
        });
        textarea.value = `Part ${part} of ${filename}:\n\n${text}`;
        textarea.dispatchEvent(enterKeyEvent);
      }
  
      // Function to check if ChatGPT is ready
      async function waitForChatGPT() {
        let chatgptReady = false;
        while (!chatgptReady) {
          await new Promise(resolve => setTimeout(resolve, 1000));
          chatgptReady = !document.querySelector(".text-2xl > span:not(.invisible)");
        }
      }
  
      // Add click event listener to the submit button
      submitButton.addEventListener('click', async () => {
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = '.txt, .js, .py, .html, .css, .json, .csv';
        input.onchange = async (event) => {
          const file = event.target.files[0];
          if (file) {
            const reader = new FileReader();
            reader.onload = async (e) => {
              const content = e.target.result;
              const chunkSize = 15000;
              const numChunks = Math.ceil(content.length / chunkSize);
              
              for (let i = 0; i < numChunks; i++) {
                const start = i * chunkSize;
                const end = (i + 1) * chunkSize;
                const chunk = content.slice(start, end);
                
                await submitConversation(chunk, i + 1, file.name);
                progressBarInner.style.width = `${((i + 1) / numChunks) * 100}%`;
              }
              
              progressBarInner.style.backgroundColor = 'blue';
              await waitForChatGPT();
            };
            reader.readAsText(file);
          }
        };
        input.click();
      });
  
    } else {
      console.error("Target element not found.");
    }
  });
  