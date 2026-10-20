import { createBrowserRouter } from "react-router-dom";

import LoginPage from "@/features/auth/pages/LoginPage";
import RegisterPage from "@/features/auth/pages/RegisterPage";
import CustomerDetailsPage from "@/features/customers/pages/CustomerDetailsPage";
import CustomersPage from "@/features/customers/pages/CustomersPage";
import DashboardPage from "@/features/dashboard/pages/DashboardPage";
import HomePage from "@/features/home/HomePage";
import AppLayout from "@/layouts/AppLayout";
import RootLayout from "@/layouts/RootLayout";

import ProtectedRoute from "./ProtectedRoute";

export const router = createBrowserRouter([
  {
    element: <RootLayout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
      },
      {
        path: "/login",
        element: <LoginPage />,
      },
      {
        path: "/register",
        element: <RegisterPage />,
      },
    ],
  },

  {
    element: <ProtectedRoute />,
    children: [
      {
        element: <AppLayout />,
        children: [
          {
            path: "/dashboard",
            element: <DashboardPage />,
          },
          {
            path: "/customers",
            element: <CustomersPage />,
          },
          {
            path: "/customers/:customerId",
            element: <CustomerDetailsPage />,
          },
        ],
      },
    ],
  },
]);