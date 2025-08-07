import React from 'react';
import BookCard from './BookCard';

interface Book {
  id: string;
  title: string;
  author: string;
  rating: number;
  reviewCount: number;
  image: string;
  genre: string;
  isLiked?: boolean;
}

const FeaturedBooks: React.FC = () => {
  // Mock data - in real app this would come from API
  const featuredBooks: Book[] = [
    {
      id: '1',
      title: 'The Midnight Library',
      author: 'Matt Haig',
      rating: 4.2,
      reviewCount: 1542,
      image: 'https://images.pexels.com/photos/1370295/pexels-photo-1370295.jpeg?auto=compress&cs=tinysrgb&w=400&h=600',
      genre: 'Fiction',
      isLiked: true
    },
    {
      id: '2',
      title: 'Atomic Habits',
      author: 'James Clear',
      rating: 4.7,
      reviewCount: 2134,
      image: 'https://images.pexels.com/photos/1130980/pexels-photo-1130980.jpeg?auto=compress&cs=tinysrgb&w=400&h=600',
      genre: 'Self-Help'
    },
    {
      id: '3',
      title: 'The Seven Husbands of Evelyn Hugo',
      author: 'Taylor Jenkins Reid',
      rating: 4.5,
      reviewCount: 3421,
      image: 'https://images.pexels.com/photos/1029141/pexels-photo-1029141.jpeg?auto=compress&cs=tinysrgb&w=400&h=600',
      genre: 'Romance'
    },
    {
      id: '4',
      title: 'Project Hail Mary',
      author: 'Andy Weir',
      rating: 4.6,
      reviewCount: 1876,
      image: 'https://images.pexels.com/photos/1481309/pexels-photo-1481309.jpeg?auto=compress&cs=tinysrgb&w=400&h=600',
      genre: 'Sci-Fi'
    }
  ];

  return (
    <section className="bg-gray-50 py-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Featured Books
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Discover the most popular and highly-rated books from our community of readers
          </p>
        </div>

        {/* Books Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          {featuredBooks.map((book) => (
            <BookCard 
              key={book.id} 
              book={book}
              onBookClick={(book) => console.log('Clicked book:', book.title)}
            />
          ))}
        </div>

        {/* View More Button */}
        <div className="text-center mt-12">
          <button className="bg-blue-600 text-white px-8 py-3 rounded-xl font-semibold hover:bg-blue-700 transition-all duration-200 transform hover:scale-105">
            View All Books
          </button>
        </div>
      </div>
    </section>
  );
};

export default FeaturedBooks;