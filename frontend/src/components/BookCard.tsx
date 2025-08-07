import React from 'react';
import { Star, Heart, MessageCircle } from 'lucide-react';

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

interface BookCardProps {
  book: Book;
  onBookClick?: (book: Book) => void;
}

const BookCard: React.FC<BookCardProps> = ({ book, onBookClick }) => {
  const renderStars = (rating: number) => {
    return Array.from({ length: 5 }, (_, i) => (
      <Star
        key={i}
        className={`w-4 h-4 ${
          i < Math.floor(rating)
            ? 'text-yellow-400 fill-yellow-400'
            : i < rating
            ? 'text-yellow-400 fill-yellow-400 opacity-50'
            : 'text-gray-300'
        }`}
      />
    ));
  };

  return (
    <div 
      className="bg-white rounded-xl shadow-md hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2 cursor-pointer group"
      onClick={() => onBookClick?.(book)}
    >
      {/* Book Cover */}
      <div className="relative overflow-hidden rounded-t-xl">
        <img
          src={book.image}
          alt={book.title}
          className="w-full h-64 object-cover group-hover:scale-110 transition-transform duration-500"
        />
        <div className="absolute top-3 right-3">
          <button className="p-2 bg-white bg-opacity-90 rounded-full shadow-md hover:bg-opacity-100 transition-all duration-200">
            <Heart className={`w-4 h-4 ${book.isLiked ? 'text-red-500 fill-red-500' : 'text-gray-600'}`} />
          </button>
        </div>
        <div className="absolute bottom-3 left-3">
          <span className="bg-blue-600 text-white px-2 py-1 rounded-full text-xs font-medium">
            {book.genre}
          </span>
        </div>
      </div>

      {/* Book Info */}
      <div className="p-6">
        <h3 className="font-bold text-lg text-gray-900 mb-2 line-clamp-2 group-hover:text-blue-600 transition-colors">
          {book.title}
        </h3>
        <p className="text-gray-600 mb-3">{book.author}</p>
        
        {/* Rating and Reviews */}
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-1">
            <div className="flex items-center">
              {renderStars(book.rating)}
            </div>
            <span className="text-sm font-medium text-gray-700 ml-1">
              {book.rating.toFixed(1)}
            </span>
          </div>
          
          <div className="flex items-center space-x-1 text-gray-500">
            <MessageCircle className="w-4 h-4" />
            <span className="text-sm">{book.reviewCount}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BookCard;