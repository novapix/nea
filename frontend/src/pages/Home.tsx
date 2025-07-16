import { Link } from 'react-router-dom'
import neaLogo from '@/assets/nea-header-logo.png'

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header className="bg-slate-800 text-white p-4">
        <div className="container mx-auto flex justify-between items-center">
          <img src={neaLogo} alt="NEA Logo" className="h-12" />
          <nav>
            <Link to="/login" className="px-4 py-2 bg-blue-600 rounded hover:bg-blue-700 transition">
              Login
            </Link>
          </nav>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow container mx-auto p-8">
        <section className="max-w-3xl mx-auto text-center">
          <h1 className="text-4xl font-bold mb-6">Welcome to NEA Billing System</h1>
          <p className="text-xl mb-8">
            Manage your billing and payments efficiently with our modern platform
          </p>
          <Link 
            to="/login" 
            className="inline-block px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
          >
            Get Started
          </Link>
        </section>
      </main>

      {/* Footer */}
      <footer className="bg-slate-800 text-white p-4 text-center">
        <p>© {new Date().getFullYear()} NEA Billing System. All rights reserved.</p>
      </footer>
    </div>
  )
}
