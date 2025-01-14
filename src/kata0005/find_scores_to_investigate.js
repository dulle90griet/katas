/* The MongoDB Atlas training database contains a collection, `grades`, in which the documents follow this schema:

```
{
  _id: ObjectId("56d5f7eb604eb380b0d8dbf3"),
  student_id: 80,
  scores: [
    { type: 'exam', score: 14.830312808539448 },
    { type: 'quiz', score: 89.44855156643018 },
    { type: 'homework', score: 83.9491981459932 },
    { type: 'homework', score: 79.42347084243777 }
  ],
  class_id: 256
}
```

The teacher of class 256 has noticed that some students received noticeably higher scores on take-home assignments than on in-person exams and quizzes. They want to investigate whether those students might have used ChatGPT (or an equivalent generative AI service) to cheat, or, conversely, whether they are genuinely better-suited to long-form take-home work.

To help identify students whose homework may warrant further inspection, use MongoDB aggregation pipelines to find all students in class 256 who, by the standards of class 256, have at least one above-average homework score, and who also have at least one homework score at least 25% higher than the average of their exam and quiz scores for the class.
*/

use('sample_training');

// Get average homework score for class 256 and assign it to a variable name

var avg_homework = db.grades.aggregate([
  {
    $match: { class_id: 256 }
  },
  {
    $unwind: "$scores"
  },
  {
    $match: { "scores.type": "homework" }
  },
  {
    $group: {
      _id: null,
      avg: { $avg: "$scores.score" }
    }
  }
]).toArray()[0]["avg"];

// console.log(`The average homework score for class 256 is ${avg_homework}.`)

// For each student, calculate the average of their exam and quiz scores for class 256

db.grades.aggregate([
  {
    $match: { class_id: 256 }
  },
  {
    $unwind: "$scores"
  },
  {
    $match: {
      "scores.type": {
        $in: ["exam", "quiz"]
      }
    }
  },
  {
    $group: {
      _id: "$student_id",
      avg_exam_quiz: { $avg: "$scores.score" }
    }
  },
  {
    $addFields: {
      comp_threshold: { $multiply: [ "$avg_exam_quiz", 1.25 ] }
    }
  },
  {
    $out: "grades_in_person_averaged"
  }
])

// Select students who have at least one homework score for class 256 which is above the average (stages 1-3 below)
// Further filter for students who have at least one homework score that is 25%+ higher than their exam-and-quiz average (stages 4-5 below)

db.grades.aggregate([
  {
    $match: { class_id: 256 }
  },
  {
    $project: {
      _id: 1,
      student_id: 1,
      homework_scores: {
        $filter: {
          input: "$scores",
          as: "item",
          cond: { $eq: ["$$item.type", "homework"] }
        }
      },
      class_id: 1
    }
  },
  {
    $match: { "homework_scores.score": { $gt: avg_homework }}
  },
  {
    $lookup: {
      from: "grades_in_person_averaged",
      localField: "student_id",
      foreignField: "_id",
      as: "grades_in_person"
    }
  },
  {
    $match: {
      $expr: {
        $gte: [
          "$homework_scores.score",
          "$grades_in_person.comp_threshold"
        ]
      }
    }
  },
  {
    $out: "class_256_scores_to_investigate"
  }
])

db.grades_in_person_averaged.drop()