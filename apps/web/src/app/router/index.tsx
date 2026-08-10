import { createBrowserRouter } from "react-router-dom";

import LoginPage from "@/features/auth/pages/LoginPage";
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