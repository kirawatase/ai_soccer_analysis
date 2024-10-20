import React, { useState, useEffect } from 'react';
import Example from './assets/example.png';
import TeamAPC from './assets/TeamAPC.png';
import TeamBPC from './assets/TeamBPC.png';
import POSS from './assets/poss.jpg';
import ASP from './assets/ASP.png';
import BSP from './assets/BSP.png';
import ATD from './assets/ATD.png';
import BTD from './assets/BTD.png';
import BVC from './assets/backgroundVideoCropped.mp4';


const Project = () => {
  const [file, setFile] = useState(null); 
  const [step, setStep] = useState(1);   
  const [showProceedButton, setShowProceedButton] = useState(false); 
  const [processingMessage, setProcessingMessage] = useState('Analysis in progress...'); 

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0]; 
    setFile(selectedFile);  
  };

  const handleProceed = () => {
    if (file) {
      setStep(2);  
      setShowProceedButton(false); 
      setProcessingMessage('Our advanced AI model is analyzing your video now! Thinking in progress...'); 
    }
  };

  const handleProceed2 = () => {
    if (file) {
      setStep(3);  
    }
  };

  useEffect(() => {
    if (step === 2) {
      const timer = setTimeout(() => {
        setShowProceedButton(true); 
        setProcessingMessage('Ready! Proceed below.'); 
      }, 5500);

      return () => clearTimeout(timer); 
    }
  }, [step]);

  return (
    <div className="font-apple bg-gray-800 min-h-screen py-16 px-8">
      <div className="max-w-4xl mx-auto text-center">
        <h1 className="text-3xl font-bold text-gray-100 mb-6">About FootyAnalysis</h1>
        <p className="text-lg leading-relaxed text-gray-100 mb-8">
          We used YOLO and Roboflow to create an advanced AI model 
          to analyze soccer videos. Our code tracks players and some parameters
          such as distance covered by team/players, max speeds of players, pass completion, and possession percentage
          etc. It gives suggestions to optimize strategy along with visualization of data. 
        </p>

        {step === 1 && (
          <div className="bg-gray-900 shadow-md rounded-lg p-6 border-4 border-gray-600 mb-8">
            <h2 className="text-2xl text-gray-100 font-bold mb-4">Step 1: Upload Match Footage</h2>
            <p className="text-lg text-gray-100 mb-4">
              Upload your recorded match footage to begin the analysis.
            </p>
            
            <input 
              type="file" 
              accept="video/mp4, video/quicktime"
              onChange={handleFileChange} 
              className="block w-full text-lg text-gray-900 border-2 border-gray-600 rounded-lg cursor-pointer bg-gray-100 p-2 focus:outline-none"
            />

            {file && (
              <p className="mt-4 text-gray-600">Uploaded File: {file.name}</p>
            )}

            {file && (
              <button 
                onClick={handleProceed}
                className="mt-4 bg-blue-500 text-white py-2 px-6 rounded-lg hover:bg-blue-600 transition duration-300"
              >
                Proceed to Step 2
              </button>
            )}
          </div>
        )}

        {step === 2 && (
          <div className="bg-gray-900 shadow-md rounded-lg p-6 border-4 border-gray-600 mb-8">
            <h2 className="text-2xl text-gray-100 font-bold mb-4">Step 2: Processing...</h2>
            <p className="text-lg text-gray-100 mb-4">
              {processingMessage}
            </p>

            {showProceedButton && (
              <button 
                onClick={handleProceed2}
                className="mt-4 bg-blue-500 text-white py-2 px-6 rounded-lg hover:bg-blue-600 transition duration-300"
              >
                Proceed to Step 3
              </button>
            )}
          </div>
        )}

        {step === 3 && (
          <div>
            <div className="bg-gray-900 shadow-md rounded-lg p-6 border-4 border-gray-600 mb-8">
              <h2 className="text-2xl text-gray-100 font-bold mb-4">Step 3: Results</h2>
              <p className="text-lg text-gray-100 mb-4">
                After using our AI models on your video, we have given you some analysis! See more below...
              </p>
            </div>

            <video 
                className="w-full max-w-md mx-auto rounded-lg border-4 border-gray-600 mb-8" 
                controls
              >
                <source src={BVC} type="video/mp4" />
                Your browser does not support the video tag.
              </video>

            <div className="text-2xl font-bold text-gray-100 mb-6">
             Max Speeds:
            </div>
            <div className="text-lg leading-relaxed text-gray-100 mb-8">
              Team 1: 
            </div>
            <img 
              src={ASP} 
              alt="Analysis Result Example" 
              className="w-full max-w-md mx-auto rounded-lg border-4 border-gray-600 mb-4"
            />
            <div className="text-lg leading-relaxed text-gray-100 mb-8">
              Team 2: 
            </div>
            <img 
              src={BSP} 
              alt="Analysis Result Example" 
              className="w-full max-w-md mx-auto rounded-lg border-4 border-gray-600 mb-12"
            />

            <div className="text-2xl font-bold text-gray-100 mb-6">
             Total Distance:
            </div>
            <div className="text-lg leading-relaxed text-gray-100 mb-8">
              Team 1: 
            </div>
            <img 
              src={ATD} 
              alt="Analysis Result Example" 
              className="w-full max-w-md mx-auto rounded-lg border-4 border-gray-600 mb-4"
            />
            <div className="text-lg leading-relaxed text-gray-100 mb-8">
              Team 2: 
            </div>
            <img 
              src={BTD} 
              alt="Analysis Result Example" 
              className="w-full max-w-md mx-auto rounded-lg border-4 border-gray-600 mb-12"
            />

            <div className="text-2xl font-bold text-gray-100 mb-6">
             Pass Completion:
            </div>
            <div className="text-lg leading-relaxed text-gray-100 mb-8">
              Team 1: 
            </div>
            <img 
              src={TeamAPC} 
              alt="Analysis Result Example" 
              className="w-full max-w-md mx-auto rounded-lg border-4 border-gray-600 mb-4"
            />
            <div className="text-lg leading-relaxed text-gray-100 mb-8">
              Team 2: 
            </div>
            <img 
              src={TeamBPC} 
              alt="Analysis Result Example" 
              className="w-full max-w-md mx-auto rounded-lg border-4 border-gray-600 mb-12"
            />

            <div className="text-2xl font-bold text-gray-100 mb-6">
             Possession Over Time:
            </div>
            <img 
              src={POSS} 
              alt="Analysis Result Example" 
              className="w-full max-w-md mx-auto rounded-lg border-4 border-gray-600 mb-4"
            />


          </div>
        )}
        <div className="relative text-center py-4 text-gray-300 z-10">
            &copy; 2024 HackOHI/O 12 Team #173 - All Rights Reserved
          </div>
      </div>
    </div>
  );
};

export default Project;
