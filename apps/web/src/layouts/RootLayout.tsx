import { Outlet } from "react-router-dom";

import Footer from "@/components/navigation/Footer";
import Navbar from "@/components/navigation/Navbar";

export default function RootLayout() {
  return (
    <div className="flex min-h-screen flex-col bg-background text-text">
      <Navbar />

      <main className="flex-1">
        <Outlet />
      </main>

      <Footer />
    </div>
  );
}