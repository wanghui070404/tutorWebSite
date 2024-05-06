function switchTab(tabId) {
    // Ẩn tất cả các tab
    var tabs = document.querySelectorAll('#personalTab, #passwordTab');
    var personal = document.getElementById('personal');
    var password = document.getElementById('password');
    tabs.forEach(function(tab) {
      if (tab.id === tabId) {
        tab.style.display = 'block';
        personal.style.color = 'blue';
        password.style.color = '#424141';
      } else {
        tab.style.display = 'none';
        password.style.color = 'blue';
        personal.style.color = '#424141';
      }
    });
}

switchTab('personalTab');

