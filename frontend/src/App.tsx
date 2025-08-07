import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Hero from './components/Hero';
import FeaturedBooks from './components/FeaturedBooks';
import Features from './components/Features';
import Footer from './components/Footer';
import Auth from './components/Auth';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Header />
        <Routes>
          <Route
            path="/"
            element={
              <>
                <Hero />
                <FeaturedBooks />
                <Features />
              </>
            }
          />
          <Route
            path="/auth"
            element={<Auth />}
          />
          <Route
            path="/browse"
            element={
              <div className="min-h-screen flex items-center justify-center">
                <div className="text-center">
                  <h1 className="text-3xl font-bold text-gray-900 mb-4">Browse Books</h1>
                  <p className="text-gray-600">This page will contain book browsing functionality</p>
                </div>
              </div>
            }
          />
          <Route
            path="/library"
            element={
              <div className="min-h-screen flex items-center justify-center">
                <div className="text-center">
                  <h1 className="text-3xl font-bold text-gray-900 mb-4">My Library</h1>
                  <p className="text-gray-600">This page will show user's personal library</p>
                </div>
              </div>
            }
          />
          <Route
            path="/reviews"
            element={
              <div className="min-h-screen flex items-center justify-center">
                <div className="text-center">
                  <h1 className="text-3xl font-bold text-gray-900 mb-4">Reviews</h1>
                  <p className="text-gray-600">This page will show all reviews</p>
                </div>
              </div>
            }
          />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
