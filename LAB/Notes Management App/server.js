const express = require("express");
const { MongoClient, ObjectId } = require("mongodb");

const app = express();
const PORT = 3000;

const client = new MongoClient("mongodb://127.0.0.1:27017");
let notesCollection;

app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));

// Home - show all notes
app.get("/", async (req, res) => {
    const notes = await notesCollection.find().toArray();
    res.render("index", { notes });
});

// Add note page
app.get("/notes/new", (req, res) => {
    res.render("new");
});

// Add note
app.post("/notes", async (req, res) => {
    const { title, content, category } = req.body;

    if (!title || !content) {
        return res.send("Title and Content are required");
    }

    await notesCollection.insertOne({
        title: title,
        content: content,
        category: category,
        createdAt: new Date()
    });

    res.redirect("/");
});

// Delete note
app.post("/notes/:id/delete", async (req, res) => {
    await notesCollection.deleteOne({
        _id: new ObjectId(req.params.id)
    });

    res.redirect("/");
});

// Connect MongoDB
async function startServer() {
    await client.connect();

    const db = client.db("notes_lab");
    notesCollection = db.collection("notes");

    console.log("Connected to MongoDB");

    app.listen(PORT, () => {
        console.log(`Server running at http://localhost:${PORT}`);
    });
}

startServer();