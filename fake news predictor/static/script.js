const toggleSwitch = document.querySelector('#dark-mode-switch');
  toggleSwitch.addEventListener('change', switchTheme);

  const theme = localStorage.getItem('theme');

  if (theme === 'dark') {
    document.documentElement.classList.add('dark');
    toggleSwitch.checked = true;
  }

  function switchTheme() {
    if (toggleSwitch.checked) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  }

//
//  realFeedbackBtn.addEventListener('click', () => {
//    const feedback = 'real';
//    const text = textField.value;
//    submitFeedback(feedback, text);
//  });
//
// fakeFeedbackBtn.addEventListener('click', () => {
//    const feedback = 'fake';
//    const text = textField.value;
//    submitFeedback(feedback, text);
//  });
//  function submitFeedback(feedback) {
//    const data = { feedback, text: document.getElementsByName("text")[0].value };
//    fetch("/feedback", {
//      method: "POST",
//      headers: {
//        "Content-Type": "application/json"
//      },
//      body: JSON.stringify(data)
//    })
//    .then(response => {
//      console.log(response);
//    })
//    .catch(error => {
//      console.error(error);
//    });
//  }


