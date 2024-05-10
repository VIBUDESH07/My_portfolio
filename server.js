var http = require("http");
var fs = require("fs");
var path = require("path");

var server = http.createServer(function (req, res) {
    if (req.url == "/home") {
        fs.readFile("My_portfolio/index.html", function (err, data) {
            if (err) {
                res.writeHead(404, { "Content-Type": "text/html" });
                res.end("<h1>404 Not Found</h1>");
            } else {
                res.writeHead(200, { "Content-Type": "text/html" });
                res.write(data);
                res.end();
            }
        });
    } 
else if (req.url === "/cgpa") {
	fs.readFile("cgpa.html", function (err, data){
        if (err) {
                res.writeHead(404, { "Content-Type": "text/html" });
                res.end("<h1>404 Not Found</h1>");
            } else {
                res.writeHead(200, { "Content-Type": "text/html" });
                res.write(data);
                res.end();
            }
});
        } 
else if (req.url === "/contact") {
	fs.readFile("contact.html", function (err, data){
        if (err) {
                res.writeHead(404, { "Content-Type": "text/html" });
                res.end("<h1>404 Not Found</h1>");
            } else {
                res.writeHead(200, { "Content-Type": "text/html" });
                res.write(data);
                res.end();
            }
});
        } 

else {
        res.writeHead(404, { "Content-Type": "text/html" });
        res.write("<h1>404 Not Found</h1>");
        res.write("<p>The requested page could not be found</p>");
        res.end();
    }
});

server.listen(1000);
console.log("Server is Running");