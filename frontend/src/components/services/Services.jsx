import { useRef, useState } from "react";
import axios from "axios";
import "./services.scss";
import { motion, useInView } from "framer-motion";

const variants = {
  initial: {
    x: -500,
    y: 100,
    opacity: 0,
  },
  animate: {
    x: 0,
    opacity: 1,
    y: 0,
    transition: {
      duration: 1,
      staggerChildren: 0.1,
    },
  },
};

const Services = () => {
  const ref = useRef();

  const isInView = useInView(ref, { margin: "-100px" });

  const [patientData, setPatientData] = useState({
    name: "",
    age: "",
    gender: "",
    history: "",
  });
  const [isPatientDataSubmitted, setIsPatientDataSubmitted] = useState(false);
  const [answers, setAnswers] = useState({});
  const [currentQuestion, setCurrentQuestion] = useState("");
  const [recommendation, setRecommendation] = useState("");
  const [instructions, setInstructions] = useState("");
  const [error, setError] = useState("");

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setPatientData({
      ...patientData,
      [name]: value,
    });
  };

  const submitPatientData = (e) => {
    e.preventDefault();
    setIsPatientDataSubmitted(true);
    // startDiagnosis();
  };

  const startDiagnosis = async () => {
    setAnswers({});
    setRecommendation("");
    setInstructions("");
    setError("");

    try {
      const response = await axios.post("http://localhost:5000/next-step", {
        answers: {},
        patient_data: patientData,
      });
      setCurrentQuestion(response.data.question);
    } catch (error) {
      setError("Error starting diagnosis");
      console.error("Error starting diagnosis :", error);
    }
  };

  const handleAnswer = async (answer) => {
    const updatedAnswers = { ...answers, [currentQuestion]: answer };
    setAnswers(updatedAnswers);
    setError("");

    try {
      const response = await axios.post("http://localhost:5000/next-step", {
        answers: updatedAnswers,
        patient_data: patientData,
      });
      if (response.data.recommendation) {
        setRecommendation(response.data.recommendation);
        setInstructions(response.data.instructions);
      } else {
        setCurrentQuestion(response.data.question);
      }
    } catch (error) {
      setError("Error fetching next step");
      console.error("Error fetching next step:", error);
    }
  };
  return (
    <motion.div
      className="services"
      variants={variants}
      initial="initial"
      ref={ref}
      animate={"animate"}
    >
      <motion.div className="textContainer" variants={variants}>
        <p>
           Our #1 Priority Is Your Happiness
          <br /> With Our Service
        </p>
        <hr />
      </motion.div>
      <motion.div className="titleContainer" variants={variants}>
        <div className="title">
          <img src="/people.webp" alt="" />
          <h1>
            <motion.b whileHover={{ color: "orange" }}>Have</motion.b> Your
          </h1>
        </div>
        <div className="title">
          <h1>
            <motion.b whileHover={{ color: "orange" }}>Injury</motion.b>{" "}
            Diagnosed
          </h1>
        </div>
      </motion.div>
      <motion.div className="listContainer" variants={variants}>
        {!isPatientDataSubmitted ? (
          <motion.form className="patientInformation" method="post">
            <h2>Please Enter Your Information</h2>
            <motion.input
              whileHover={{
                scale: 1.2,
                transition: { duration: 1 },
              }}
              type="text"
              name="name"
              placeholder="Name"
              onChange={handleInputChange}
              value={patientData.name}
              required
            ></motion.input>
            <motion.input
              whileHover={{
                scale: 1.2,
                transition: { duration: 1 },
              }}
              type="number"
              name="age"
              placeholder="Age"
              onChange={handleInputChange}
              value={patientData.age}
              required
            ></motion.input>
            <select
              name="gender"
              placeholder="Gender"
              onChange={handleInputChange}
              value={patientData.gender}
              required
            >
              <option disabled selected value="">select an option</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
            </select>
            <motion.input
              whileHover={{
                scale: 1.2,
                transition: { duration: 1 },
              }}
              type="text"
              name="history"
              placeholder="History of Disease"
              onChange={handleInputChange}
              value={patientData.history}
              required
            ></motion.input>
            <button onClick={submitPatientData}>Submit</button>
          </motion.form>
        ) : recommendation ? (
          <motion.div
            className="result-section"
            animate={{ x: [0, 100, 0], y: [100, 0, 0] }}
          >
            <h2>Recommendation</h2>
            <p>{recommendation}</p>
            <h3>Instruction</h3>
            <p>{instructions}</p>
          </motion.div>
        ) : (
          <motion.div className="question-section">
            {currentQuestion ? (
              <motion.div
                className="question-box"
                key={currentQuestion}
                initial={{ opacity: 0, y: 50 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -50 }}
              >
                <h2>{currentQuestion}</h2>
                <div className="buttons">
                  <button onClick={() => handleAnswer("yes")}>Yes</button>
                  <button onClick={() => handleAnswer("no")}>No</button>
                </div>
              </motion.div>
            ) : (
              <motion.button
                animate={{ x: 50 }}
                transition={{ ease: "easeOut", duration: 2 }}
                className="diagnosis-button"
                onClick={startDiagnosis}
              >
                Start Diagnosis
              </motion.button>
            )}
          </motion.div>
        )}
      </motion.div>
    </motion.div>
  );
};

export default Services;
