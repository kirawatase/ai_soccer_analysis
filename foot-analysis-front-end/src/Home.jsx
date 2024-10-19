import React from 'react';
import pepGuardiolaImage from './assets/pepGuardiolaManCityAI.jpg';

const Home = () => {
  return (
    <div className="bg-gray-100 min-h-screen flex flex-col items-center m-0">
      <div className="flex justify-center mt-12">
        <img 
          src={pepGuardiolaImage} 
          alt="Pep Guardiola using our project" 
          className="w-80 h-auto shadow-lg hover:shadow-xl transition-shadow duration-300" 
        />
      </div>

      <div className="flex flex-col items-center mt-6 px-8 py-16 text-center font-tech text-lg leading-relaxed font-normal max-w-4xl mx-auto">
        <div className="text-3xl font-bold mb-4">
          Revolutionize Your Game with AI
        </div>

        <div className="text-justify">
          Welcome to the future of soccer analysis! Our AI-powered software takes your match videos and delivers deep, actionable insights to enhance performance and strategy.
          No matter if you're a coach or player, this platform will provide the analysis you need to elevate your game to the next level.
          <br /><br />
          <span className="text-blue-400 font-semibold">
            Ready for more information? Head over to the "The Project" tab to learn more about how it works!
          </span>
        </div>
      </div>

      <div className="text-center py-4 text-gray-600">
        &copy; 2024 HackOHI/O 12 Team #173 - All Rights Reserved
      </div>
    </div>
  );
};

export default Home;
