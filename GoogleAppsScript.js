function checkTickets(url) {
  console.log(url);
  var KEYWORD = "【开票】";
  var options = {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
  };
  var response = UrlFetchApp.fetch(url, options);
  var content = response.getContentText();
  if (content.includes(KEYWORD)) {
    var concertTitle = getConcertTitle(content);
    console.log(concertTitle);
    console.log('tickets!!!');
    // You can use other methods to notify in Google Apps Script, such as sending an email.
    // For simplicity, let's just log the notification here.
    console.log('chncpa ticket is open: ' + concertTitle);

    // Send an email notification
    var subject = 'chncpa ticket is open';
    var body = concertTitle + '\n' + url;
    sendEmail(subject, body);    

    Utilities.sleep(5000);
  } else {
    console.log('please wait');
  }
}

function sendEmail(subject, body) {
  var recipient = 'XXX'; // Replace with your email address
  GmailApp.sendEmail(recipient, subject, body);
}

function getConcertTitle(html) {
  var titleMatch = html.match(/<title[^>]*>([^<]*)<\/title>/i);
  if (titleMatch && titleMatch.length >= 2) {
    return titleMatch[1];
  } else {
    return 'Title Not Found';
  }
}

function getTextFromGoogleDocs(fileId) {
  var doc = DocumentApp.openById(fileId);
  var body = doc.getBody();
  var text = body.getText();
  return text;
}


function main() {
  
  var ticketListFileId = 'XXX';  // Replace with the actual file ID.
  var fileContent = getTextFromGoogleDocs(ticketListFileId);
  var urls = fileContent.split('\n');
  for (var i = 0; i < urls.length; i++) {
    checkTickets(urls[i]);
  }
}
