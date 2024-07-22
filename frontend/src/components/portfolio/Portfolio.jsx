import { useRef } from "react";
import "./portfolio.scss";
import { motion, useScroll, useSpring, useTransform } from "framer-motion";

const items = [
  {
    id: 1,
    title: "Time and money",
    img: "/s1.svg",
    desc: "Online sessions are much faster and more flexible, so you don’t need to take time off work, or spend on travel.",
  },
  {
    id: 2,
    title: "Environmentally-friendly",
    img: "/s2.svg",
    desc: "There’s no need to travel, which supports our commitment to being carbon negative.",
  },
  {
    id: 3,
    title: "No waiting list",
    img: "/s3.svg",
    desc: "You receive treatment when you need it rather than waiting for weeks or months on end.",
  },
  {
    id: 4,
    title: "Geographical obstacle removed",
    img: "/s4.svg",
    desc: "You can access leading physiotherapy specialists in your area of injury from wherever you are in the country, or world!",
  },
];

const Single = ({ item }) => {
  const ref = useRef();

  const { scrollYProgress } = useScroll({
    target: ref,
  });

  const y = useTransform(scrollYProgress, [0, 1], [-300, 300]);

  return (
    <section >
      <div className="container">
        <div className="wrapper">
          <div className="imageContainer" ref={ref}>
            <img src={item.img} alt="" />
          </div>
          <motion.div className="textContainer" style={{y}}>
            <h2>{item.title}</h2>
            <p>{item.desc}</p>
          </motion.div>
        </div>
      </div>
    </section>
  );
};

const Portfolio = () => {
  const ref = useRef();

  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["end end", "start start"],
  });

  const scaleX = useSpring(scrollYProgress, {
    stiffness: 100,
    damping: 30,
  });

  return (
    <div className="portfolio" ref={ref}>
      <div className="progress">
        <h1>The Benefits of Physio</h1>
        <motion.div style={{ scaleX }} className="progressBar"></motion.div>
      </div>
      {items.map((item) => (
        <Single item={item} key={item.id} />
      ))}
    </div>
  );
};

export default Portfolio;
