import React from 'react';
import { Link } from 'react-router-dom';  

const Navbar = () => {
  return (
    <nav className="bg-gray-900 p-4">
      <div className="flex justify-center">
        <ul className="flex space-x-12 text-gray-100 font-semibold font-apple text-xl">
          <li>
            <Link 
              to="/" 
              className="hover:text-gray-300 border-gray-600 hover:bg-gray-700 transition px-4 py-2"
            >
              Home
            </Link>
          </li>
          <li>
            <Link 
              to="/project" 
              className="hover:text-gray-300 border-gray-600 hover:bg-gray-700 transition px-4 py-2"
            >
              The Project
            </Link>
          </li>
          <li>
            <Link 
              to="/team" 
              className="hover:text-gray-300 border-gray-600 hover:bg-gray-700 transition px-4 py-2"
            >
              Our Team
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;

//old code

// import React from 'react';

// const Navbar = () => {
//   return (
//     <nav className="bg-blue-400 p-4">
//       <div className="flex justify-center">
//         <ul className="flex space-x-12 text-gray-100 font-semibold font-tech text-xl">
//           <li><a href="/" className="hover:text-gray-300 border border-gray-100 rounded-md px-4 py-2 hover:bg-blue-500 transition">Home</a></li>
//           <li><a href="/project" className="hover:text-gray-300 border border-gray-100 rounded-md px-4 py-2 hover:bg-blue-500 transition">The Project</a></li>
//           <li><a href="/team" className="hover:text-gray-300 border border-gray-100 rounded-md px-4 py-2 hover:bg-blue-500 transition">Our Team</a></li>
//         </ul>
//       </div>
//     </nav>
//   );
// };

// export default Navbar;
