import React from "react";

const CircularProgress = ({Reason, progress}) => {
  const radius = 60;
  const stroke = 12;
  const normalizedRadius = radius - stroke * 0.5;
  const circumference = normalizedRadius * 2 * Math.PI;
  const strokeDashoffset =
    circumference - (progress / 100) * circumference;

  // Compute color based on progress
  const getColor = (p) => {
    if (p < 50) {
      const green = Math.round((p / 50) * 255);
      return `rgb(255, ${green}, 0)`; 
    } else {
      const red = Math.round(255 - ((p - 50) / 50) * 255);
      return `rgb(${red}, 255, 0)`; 
    }
  };

  const color = getColor(progress);

  const getMessage = (p) => {
    if (p < 25) return (<span className="text-red-600">⚠️ Risk Error Detcted</span>);
    if (p < 40) return (<span className="text-red-600">❌ Warning</span>);
    if (p < 60) return (<span className="text-yellow-500">❓ Suspicious Potential Threat</span>);
    if (p < 75) return (<span className="text-green-600">✅ Good</span>);
    if (p < 100) return (<span className="text-blue-600">🌟 Excellent</span>);
    return "Completed!";
  };
 
  return (
    <div className="slide flex gap-10 sm:gap-0   sm:flex-col items-center space-y-4">
      <div className="relative  RollAndGrow ">
        <svg
          height={radius * 2}
          width={radius * 2}
          className="transform -rotate-90 Roll"
        >
          <circle
            stroke="#e5e7eb"
            fill="transparent"
            strokeWidth={stroke}
            r={normalizedRadius}
            cx={radius}
            cy={radius}
          />
          <circle
            stroke={color}
            fill="transparent"
            strokeWidth={stroke}
            strokeLinecap="round"
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
            r={normalizedRadius}
            cx={radius}
            cy={radius}
            className="transition-all duration-500 ease-out"
          />
        </svg>
        <div
          className="absolute inset-0 flex items-center justify-center text-2xl font-bold"
          style={{ color }}
        >
          {progress}%
        </div>
      </div>
      <h2 className="text-2xl font-medium mt-5" style={{ color }}>
        {getMessage(progress)}
      </h2>
      <div className=" text-lg font-medium text-reveal-container">
      <div className="reveal-text space-x-2 text-md text-blue-500">
      <p>Passed {progress}% of safety check </p>
      <p> risk : {getMessage(progress)}</p>
       {Reason || <div>{Reason}</div>}
        </div>
      </div>
    </div>
  );
};

export default CircularProgress;
