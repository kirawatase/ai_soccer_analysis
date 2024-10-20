import React from 'react';
import backgroundVideo from './assets/backgroundVideoCropped.mp4';
import IMG_0327 from './assets/IMG_0327.png';  // Import your images here

const Home = () => {
  const testimonial = {
    name: 'Mark Thompson',
    role: 'Coach',
    description: 'Four-time state winning coach',
    quote: 'As a four-time state-winning champion coach, I’ve always believed that success comes from not just hard work but also smart work. Incorporating AI-powered data visualization into our soccer analysis has transformed how we approach the game. The ability to track player positioning, distance, and in-game decisions in real time has given us insights beyond what the naked eye can see. It allows us to break down plays, adjust formations, and optimize strategies with precision. I find this very applicable to our game.'
  };

  return (
    <div className="relative w-full flex flex-col m-0">
      {/* Video Background */}
      <div className="relative w-full h-[85vh] overflow-hidden -z-20">
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
        <div className="text-5xl font-bold mb-8 text-white">
          Level Up Your Game with AI
        </div>

        <div className="text-center text-white max-w-2xl">
          The future of soccer analysis is here! Our AI-powered software takes your match videos and delivers deep, actionable insights to enhance performance and strategy. 
          Regardless of if you're a coach or player, this platform will provide all analysis you need to elevate your game to the next level.
          <br /><br />
          <span className="text-center font-apple">
            Ready for more information? Head over to the "The Project" tab to learn more about how it works!
          </span>
        </div>
      </div>

      {/* Motivations Section */}
      <div className="bg-gray-900 w-full pt-20">
        <div className="text-5xl font-bold mb-4 text-white flex justify-center">
          Our Motivations
        </div>

        <div className="relative flex flex-col text-gray-100 items-center justify-center mt-6 px-8 py-16 text-center font-apple text-lg leading-relaxed font-normal max-w-4xl mx-auto z-10">
            All my life I knew one thing. Soccer. Day in, day out, I lived and breathed strategies and techniques and pushed myself to the absolute limit.
            I played against people older than me. I played against boys. I played D1 at OSU. All the odds were stacked against me but I stood my
            ground and even excelled. Life however, had other plans. I was injured and forced into medical retirement. I was lost without direction. However, 
            I will not let the strategies and techniques I've perfected over countless years go to waste. I have found new passion in mathematics, AI, and coding.
            It is time to pass on my torch and this is my way of doing it.
        </div>
      </div>

      {/* Testimonial Section */}
      <div className="bg-gray-800 w-full py-20">
        <div className="text-5xl font-bold text-white text-center mb-8">
          Testimonial
        </div>

        <div className="flex flex-col items-center text-center max-w-2xl mx-auto">
          <p className="text-lg italic text-gray-300 mb-4">
            "{testimonial.quote}"
          </p>
          <h3 className="text-xl font-semibold text-white">{testimonial.name}</h3>
          <p className="text-gray-400">{testimonial.role}</p>
          <p className="mt-4 text-gray-300">{testimonial.description}</p>
        </div>
      </div>

      {/* Footer */}
      <div className="relative text-center py-4 text-gray-300 z-10">
        &copy; 2024 HackOHI/O 12 Team #173 - All Rights Reserved
      </div>
    </div>
  );
};

export default Home;
