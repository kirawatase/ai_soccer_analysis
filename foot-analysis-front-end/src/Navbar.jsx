import React from 'react';

const Navbar = () => {
  return (
    <nav className="bg-blue-400 p-4">
      <div className="flex justify-center">
        <ul className="flex space-x-12 text-gray-100 font-semibold font-tech text-xl">
          <li>
            <a href="/" className="hover:text-gray-300 border border-gray-100 rounded-lg px-4 py-2 hover:bg-blue-500 transition">
              Home
            </a>
          </li>
          <li>
            <a href="/project" className="hover:text-gray-300 border border-gray-100 rounded-lg px-4 py-2 hover:bg-blue-500 transition">
              The Project
            </a>
          </li>
          <li>
            <a href="/team" className="hover:text-gray-300 border border-gray-100 rounded-lg px-4 py-2 hover:bg-blue-500 transition">
              Our Team
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
