import { z } from "zod";

export const registerSchema = z
  .object({
    firstName: z
      .string()
      .trim()
      .min(1, "First name is required")
      .max(100, "First name must be at most 100 characters"),

    lastName: z
      .string()
      .trim()
      .min(1, "Last name is required")
      .max(100, "Last name must be at most 100 characters"),

    username: z
      .string()
      .trim()
      .min(3, "Username must be at least 3 characters")
      .max(50, "Username must be at most 50 characters"),

    email: z
      .string()
      .trim()
      .email("Please enter a valid email address"),

    password: z
      .string()
      .min(8, "Password must be at least 8 characters")
      .max(128, "Password must be at most 128 characters"),

    confirmPassword: z.string(),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Passwords do not match",
    path: ["confirmPassword"],
  });

export type RegisterFormData = z.infer<typeof registerSchema>;
