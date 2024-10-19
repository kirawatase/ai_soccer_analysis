import React from 'react';
import IMG_0327 from './assets/IMG_0327.png';

const Team = () => {
  const teamMembers = [
    {
      name: 'Andy Liu',
      role: 'Mathematics',
      description: 'Andy is a theoretical math major who developed the majority of the front-end for the project as well as making many stylistic decisions.',
      image: 'https://via.placeholder.com/150',  // Replace with actual image URL
    },
    {
      name: 'Kira Watase',
      role: 'Mathematics',
      description: 'Kira is the core of our team and the original D1 soccer player and math major who came up with the idea. She is responsible for much of the AI and data analysis.',
      image: IMG_0327,  // Replace with actual image URL
    },
    {
      name: 'Dylan Jian',
      role: 'Computer Science',
      description: 'Dylan is a computer science major who developed the majority of the back-end and how we are implementing the AI to connect to our front end.',
      image: 'https://via.placeholder.com/150',  // Replace with actual image URL
    },
  ];

  return (
    <div className="font-apple bg-gray-800 min-h-screen flex flex-col items-center m-0">
      <div className="text-center mt-12 text-gray-100">
        <h1 className="text-4xl font-bold mb-8">Meet Our Team</h1>
        <p className="mt-4 text-lg">
          Our team consists of three passionate technologists with a love for soccer!
        </p>
      </div>

      {/* Team Members */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 mt-12 px-8 max-w-7xl">
        {teamMembers.map((member, index) => (
          <div key={index} className="bg-gray-700 rounded-lg p-6 text-center shadow-lg hover:shadow-xl transition-shadow duration-300">
            <img
              src={member.image}
              alt={member.name}
              className="w-32 h-32 mx-auto rounded-full mb-4"
            />
            <h3 className="text-xl font-semibold text-white">{member.name}</h3>
            <p className="text-gray-400">{member.role}</p>
            <p className="mt-4 text-gray-300">{member.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Team;

