function loadInNuke(file) {    
  try {
    var content = escape(file)
    var req = new XMLHttpRequest();
    req.open('POST', "/load", true);
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.setRequestHeader("Content-length", content.length);
    req.setRequestHeader("Connection", "close");
    req.send(content);
  } catch(e) {
    alert("loadInNuke failed: " + e);
  }
}
