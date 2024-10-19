import React, { useRef } from 'react';
import useIntersectionObserver from './useIntersectionObserver';
import backgroundVideo from './assets/backgroundVideoCropped.mp4';


const Home = () => {
  return (
    <div className="relative w-full flex flex-col m-0">
      {/* Video Background */}
      <div className="relative w-full h-[85h] overflow-hidden -z-20">
        <video
          className="w-full h-[85vh] object-cover"
          style={{ objectPosition: 'center' }}  // Ensures center alignment of video
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

      {/* Text Content Overlay */}
      <div className="absolute top-0 left-0 w-full h-[85vh] flex flex-col items-center justify-center px-8 text-center font-apple text-lg leading-relaxed font-normal z-10">
        <div className="text-5xl font-bold mb-8 text-white">  {/* Increased bottom margin */}
          Level Up Your Game with AI
        </div>

        <div className="text-center text-white max-w-2xl">  {/* Max width for better centering */}
          The future of soccer analysis is here! Our AI-powered software takes your match videos and delivers deep, actionable insights to enhance performance and strategy. 
          Regardless of if you're a coach or player, this platform will provide all analysis you need to elevate your game to the next level.
          <br /><br />
          <span className="text-center font-apple">
            Ready for more information? Head over to the "The Project" tab to learn more about how it works!
          </span>
        </div>
      </div>

      {/* Motivations Section */}
      <div className="bg-gray-900 w-full pt-20 ">  {/* Added padding-top of 10 */}
        <div className="text-5xl font-bold mb-4 text-white flex justify-center">
          Our Motivations
        </div>

        <div className="relative flex flex-col text-gray-100   items-center justify-center mt-6 px-8 py-16 text-center font-apple text-lg leading-relaxed font-normal max-w-4xl mx-auto z-10">
            All my life I knew one thing. Soccer. Day in, day out, I lived and breathed strategies and techniques and pushed myself to the absolute limit.
            I played against people older than me. I played against boys. I played D1 at OSU. All the odds were stacked against me but I stood my
            ground and even excelled. Life however, had other plans. I was injured and forced into medical retirement. I was lost without direction. However, 
            I will not let the strategies and techniques I've perfected over countless years go to waste. I have found new passion in mathematics, AI, and coding.
            It is time to pass on my torch and this is my way of doing it.
        </div>

        {/* Footer */}
        <div className="relative text-center py-4 text-gray-300 z-10">
          &copy; 2024 HackOHI/O 12 Team #173 - All Rights Reserved
        </div>
      </div>
    </div>
  );
};

export default Home;
