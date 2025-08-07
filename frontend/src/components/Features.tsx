import React from 'react';
import { Star, Search, Users, BookOpen, TrendingUp, Award } from 'lucide-react';

const Features: React.FC = () => {
  const features = [
    {
      icon: Star,
      title: 'Rate & Review',
      description: 'Share your honest opinions and help others discover great books with detailed ratings and reviews.'
    },
    {
      icon: Search,
      title: 'Smart Discovery',
      description: 'Find your next favorite book with our intelligent recommendation system based on your preferences.'
    },
    {
      icon: Users,
      title: 'Community Driven',
      description: 'Join a passionate community of readers, follow friends, and discover books through social connections.'
    },
    {
      icon: BookOpen,
      title: 'Personal Library',
      description: 'Create custom reading lists, track your progress, and organize your books across multiple shelves.'
    },
    {
      icon: TrendingUp,
      title: 'Reading Stats',
      description: 'Track your reading habits, set goals, and see detailed analytics of your reading journey.'
    },
    {
      icon: Award,
      title: 'Curated Lists',
      description: 'Explore expertly curated book lists, awards, and trending titles across all genres.'
    }
  ];

  return (
    <section className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Everything You Need to Discover Great Books
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            From personalized recommendations to community reviews, we've built the ultimate platform 
            for book lovers to connect, discover, and share their reading experiences.
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div 
              key={index}
              className="group p-8 bg-white rounded-2xl border border-gray-100 hover:border-blue-200 hover:shadow-xl transition-all duration-300"
            >
              {/* Icon */}
              <div className="w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-blue-600 group-hover:scale-110 transition-all duration-300">
                <feature.icon className="w-8 h-8 text-blue-600 group-hover:text-white transition-colors duration-300" />
              </div>

              {/* Content */}
              <h3 className="text-xl font-bold text-gray-900 mb-3 group-hover:text-blue-600 transition-colors duration-300">
                {feature.title}
              </h3>
              <p className="text-gray-600 leading-relaxed">
                {feature.description}
              </p>
            </div>
          ))}
        </div>

        {/* CTA Section */}
        <div className="mt-16 text-center">
          <div className="bg-gradient-to-r from-blue-600 to-blue-800 rounded-3xl p-12 text-white">
            <h3 className="text-2xl md:text-3xl font-bold mb-4">
              Ready to Start Your Reading Journey?
            </h3>
            <p className="text-blue-100 mb-8 max-w-2xl mx-auto text-lg">
              Join thousands of readers who are already discovering amazing books and sharing their experiences.
            </p>
            <button className="bg-yellow-500 hover:bg-yellow-600 text-gray-900 font-bold py-4 px-8 rounded-xl text-lg transition-all duration-200 transform hover:scale-105">
              Get Started Now
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Features;