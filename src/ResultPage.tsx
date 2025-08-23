import React from "react";

const CircularProgress = ({ progress }) => {
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
    if (p < 30) return "Keep going!";
    if (p < 70) return "Good progress!";
    if (p < 100) return "Almost there!";
    return "Completed!";
  };

  return (
    <div className="flex flex-col items-center space-y-4">
      <div className="relative">
        <svg
          height={radius * 2}
          width={radius * 2}
          className="transform -rotate-90"
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
      <p className="text-lg font-medium" style={{ color }}>
        {getMessage(progress)}
      </p>
    </div>
  );
};

export default CircularProgress;
