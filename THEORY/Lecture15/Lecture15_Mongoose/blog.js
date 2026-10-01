const mongoose = require("mongoose");


// =====================================
// CONNECT TO MONGODB
// =====================================

mongoose.connect("mongodb://127.0.0.1:27017/blog_database")

    .then(() => {
        console.log("MongoDB connected successfully!");
        runValidationTest();
    })

    .catch((error) => {
        console.log("MongoDB connection failed!");
        console.log(error);
    });


// =====================================
// POST SCHEMA WITH VALIDATION
// =====================================

const postSchema = new mongoose.Schema({

    title: {
        type: String,
        required: [true, "Title is required"],
        minlength: [3, "Title must be at least 3 characters"],
        maxlength: [100, "Title cannot exceed 100 characters"]
    },

    content: {
        type: String,
        required: [true, "Content is required"],
        minlength: [10, "Content must be at least 10 characters"]
    },

    author: {
        type: String,
        required: [true, "Author is required"],
        minlength: [2, "Author must be at least 2 characters"],
        maxlength: [50, "Author cannot exceed 50 characters"]
    },

    createdAt: {
        type: Date,
        default: Date.now
    }

});


// =====================================
// COMMENT SCHEMA WITH VALIDATION
// =====================================

const commentSchema = new mongoose.Schema({

    postId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Post",
        required: [true, "Post ID is required"]
    },

    author: {
        type: String,
        required: [true, "Comment author is required"],
        minlength: [2, "Author must be at least 2 characters"]
    },

    text: {
        type: String,
        required: [true, "Comment text is required"],
        minlength: [3, "Comment must be at least 3 characters"]
    },

    createdAt: {
        type: Date,
        default: Date.now
    }

});


// =====================================
// CREATE MODELS
// =====================================

const Post = mongoose.model("Post", postSchema);

const Comment = mongoose.model(
    "Comment",
    commentSchema
);


// =====================================
// VALIDATION TEST
// =====================================

async function runValidationTest() {

    try {

        // Valid Post
        const validPost = new Post({

            title: "Learning Mongoose",

            content: "Mongoose provides an easy way to work with MongoDB.",

            author: "Anant"

        });

        await validPost.save();

        console.log("\nValid post created successfully!");

        console.log(validPost);


        // Valid Comment
        const validComment = new Comment({

            postId: validPost._id,

            author: "Student",

            text: "Very useful explanation!"

        });

        await validComment.save();

        console.log("\nValid comment created successfully!");

        console.log(validComment);

    }

    catch (error) {

        console.log("\nValidation Error:");

        console.log(error.message);

    }

    finally {

        await mongoose.connection.close();

        console.log("\nMongoDB connection closed.");

    }
}