import React from 'react';
import backgroundVideo from './assets/backgroundVideo.mp4';

const Home = () => {
  return (
    <div className="relative w-full flex flex-col items-center justify-center m-0">
      {/* Cropped Video Background */}
      <div className="absolute top-0 left-0 w-full overflow-hidden -z-20">
        <video
          className="w-full h-full object-cover transform translate-y-[-15%]"
          src={backgroundVideo}
          autoPlay 
          loop 
          muted 
          playsInline
        >
        </video>
      </div>

      {/* Dark Tint Overlay */}
      <div className="absolute top-0 left-0 w-full h-full bg-black opacity-50 -z-10"></div>

      {/* Content Overlay */}
      <div className="relative flex flex-col items-center justify-center mt-6 px-8 py-16 text-center font-apple text-lg leading-relaxed font-normal max-w-4xl mx-auto z-10">
        <div className="text-5xl font-bold mb-4 text-white">
          Level Up Your Game with AI
        </div>

        <div className="text-center text-white">
          The future of soccer analysis is here! Our AI-powered software takes your match videos and delivers deep, actionable insights to enhance performance and strategy. 
          Regardless of if you're a coach or player, this platform will provide all analysis you need to elevate your game to the next level.
          <br /><br />
          <span className="text-center font-apple">
            Ready for more information? Head over to the "The Project" tab to learn more about how it works!
          </span>
        </div>
      </div>
      {/* Gap before Statistics */}
      <div className="mt-40 text-5xl font-bold mb-4 text-white">
        Our Motivations
        
      </div>

      <div className="text-center text-white">
          I was
      </div>

      {/* Footer */}
      <div className="relative text-center py-4 text-gray-300 z-10">
        &copy; 2024 HackOHI/O 12 Team #173 - All Rights Reserved
      </div>
    </div>
  );
};

export default Home;