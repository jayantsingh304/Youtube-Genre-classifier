chrome.tabs.getSelected(null, function(var tab) {
         tab = tab.id;
        tabUrl = tab.url;

        alert(tab.url);
    });