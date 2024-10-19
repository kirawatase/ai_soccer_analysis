import React from 'react';

const Team = () => {
  return (
    <div className="font-apple bg-gray-800 min-h-screen flex flex-col items-center m-0">
      <div className="text-center mt-12 text-gray-100">
        <h1 className="text-3xl font-bold">Meet Our Team</h1>
        <p className="mt-4 text-lg">
          Our team consists of three passionate technologists with passion for soccer!
        </p>
      </div>
      <div className="relative text-center py-4 text-gray-300 z-10">
          &copy; 2024 HackOHI/O 12 Team #173 - All Rights Reserved
        </div>
    </div>
  );
};

export default Team;
