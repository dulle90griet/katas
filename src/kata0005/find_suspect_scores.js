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

The teacher of class 256 believes that some students who received noticeably higher scores on take-home assignments than on in-person exams and quizzes may have used ChatGPT (or an equivalent generative AI service) to cheat.

To help identify students whose homework may warrant further inspection, use MongoDB aggregation pipelines to find all students in class 256 who, by the standards of class 256, have at least one above-average homework score, and who also have at least one homework score at least 25% higher than the average of their exam and quiz scores for the class.
*/
