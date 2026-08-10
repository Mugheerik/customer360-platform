import { api } from "@/lib/api/client";

import type {
  Customer,
  CustomerCreate,
  CustomerListParams,
  CustomerListResponse,
  CustomerTimelineItem,
  CustomerUpdate,
} from "../types/customer.types";

export const CustomerService = {
  async getCustomers(
    params?: CustomerListParams,
  ): Promise<CustomerListResponse> {
    const response = await api.get<CustomerListResponse>(
      "/customers",
      {
        params,
      },
    );

    return response.data;
  },

  async getCustomer(
    customerId: string,
  ): Promise<Customer> {
    const response = await api.get<Customer>(
      `/customers/${customerId}`,
    );

    return response.data;
  },

  async createCustomer(
    data: CustomerCreate,
  ): Promise<Customer> {
    const response = await api.post<Customer>(
      "/customers",
      data,
    );

    return response.data;
  },

  async updateCustomer(
    customerId: string,
    data: CustomerUpdate,
  ): Promise<Customer> {
    const response = await api.patch<Customer>(
      `/customers/${customerId}`,
      data,
    );

    return response.data;
  },

  async activateCustomer(
    customerId: string,
  ): Promise<Customer> {
    const response = await api.patch<Customer>(
      `/customers/${customerId}/activate`,
    );

    return response.data;
  },

  async deactivateCustomer(
    customerId: string,
  ): Promise<Customer> {
    const response = await api.delete<Customer>(
      `/customers/${customerId}`,
    );

    return response.data;
  },

  async getCustomerTimeline(
    customerId: string,
  ): Promise<CustomerTimelineItem[]> {
    const response =
      await api.get<CustomerTimelineItem[]>(
        `/customers/${customerId}/timeline`,
      );

    return response.data;
  },
};