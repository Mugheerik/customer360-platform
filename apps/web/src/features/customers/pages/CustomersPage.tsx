import {
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";
import { useState } from "react";

import Button from "@/components/ui/button";
import Card from "@/components/ui/card";
import Container from "@/components/ui/container";
import Section from "@/components/ui/section";
import { Body, H1, Lead } from "@/components/ui/typography";

import { CustomerService } from "@/features/customers/api/customer.api";
import CustomerForm from "@/features/customers/components/CustomerForm";
import CustomerTable from "@/features/customers/components/CustomerTable";
import type {
  CustomerCreate,
  CustomerListParams,
  CustomerStatus,
} from "@/features/customers/types/customer.types";

export default function CustomersPage() {
  const queryClient = useQueryClient();

  const [showForm, setShowForm] = useState(false);
  const [error, setError] = useState<string | null>(
    null,
  );

  const [search, setSearch] = useState("");
  const [status, setStatus] =
    useState<CustomerStatus | "all">("all");

  const [page, setPage] = useState(1);
  const [size, setSize] = useState(20);

  const queryParams: CustomerListParams = {
    search: search.trim() || undefined,
    status:
      status === "all"
        ? undefined
        : status,
    page,
    size,
  };

  const customersQuery = useQuery({
    queryKey: ["customers", queryParams],
    queryFn: () =>
      CustomerService.getCustomers(queryParams),
  });

  const createCustomerMutation = useMutation({
    mutationFn: (data: CustomerCreate) =>
      CustomerService.createCustomer(data),

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: ["customers"],
      });

      setShowForm(false);
      setError(null);
    },

    onError: () => {
      setError("Unable to create customer.");
    },
  });

  const deactivateCustomerMutation = useMutation({
    mutationFn: (customerId: string) =>
      CustomerService.deactivateCustomer(
        customerId,
      ),

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: ["customers"],
      });

      setError(null);
    },

    onError: () => {
      setError("Unable to deactivate customer.");
    },
  });

  const activateCustomerMutation = useMutation({
    mutationFn: (customerId: string) =>
      CustomerService.activateCustomer(
        customerId,
      ),

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: ["customers"],
      });

      setError(null);
    },

    onError: () => {
      setError("Unable to activate customer.");
    },
  });

  function handleCreateCustomer(
    data: CustomerCreate,
  ) {
    setError(null);

    createCustomerMutation.mutate(data);
  }

  function handleSearchChange(
    value: string,
  ) {
    setSearch(value);
    setPage(1);
  }

  function handleStatusChange(
    value: CustomerStatus | "all",
  ) {
    setStatus(value);
    setPage(1);
  }

  function handlePageSizeChange(
    value: number,
  ) {
    setSize(value);
    setPage(1);
  }

  function handleDeactivate(
    customerId: string,
  ) {
    const confirmed = window.confirm(
      "Are you sure you want to deactivate this customer?",
    );

    if (!confirmed) {
      return;
    }

    setError(null);

    deactivateCustomerMutation.mutate(
      customerId,
    );
  }

  function handleActivate(
    customerId: string,
  ) {
    const confirmed = window.confirm(
      "Are you sure you want to activate this customer?",
    );

    if (!confirmed) {
      return;
    }

    setError(null);

    activateCustomerMutation.mutate(
      customerId,
    );
  }

  const customers =
    customersQuery.data?.items ?? [];

  const total =
    customersQuery.data?.total ?? 0;

  const totalPages =
    customersQuery.data?.pages ?? 1;

  const isUpdatingStatus =
    deactivateCustomerMutation.isPending ||
    activateCustomerMutation.isPending;

  const isFirstPage = page <= 1;
  const isLastPage = page >= totalPages;

  const firstItem =
    customers.length === 0
      ? 0
      : (page - 1) * size + 1;

  const lastItem = Math.min(
    page * size,
    total,
  );

  return (
    <Section>
      <Container>
        <div className="flex flex-col gap-6 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <H1>Customers</H1>

            <Lead className="mt-3">
              Manage customer records across the
              Customer360 platform.
            </Lead>

            <Body className="mt-2 max-w-2xl text-text-secondary">
              Create customers, review customer
              information, and manage customer
              status.
            </Body>
          </div>

          <Button
            type="button"
            onClick={() => {
              setShowForm(
                (current) => !current,
              );
              setError(null);
            }}
          >
            {showForm
              ? "Cancel"
              : "Add Customer"}
          </Button>
        </div>

        {error && (
          <Card className="mt-6 border-danger/30 bg-red-50 p-4">
            <p className="text-sm text-danger">
              {error}
            </p>
          </Card>
        )}

        {showForm && (
          <div className="mt-8">
            <CustomerForm
              onSubmit={
                handleCreateCustomer
              }
              isSubmitting={
                createCustomerMutation.isPending
              }
            />
          </div>
        )}

        <Card className="mt-8 p-4">
          <div className="grid gap-4 sm:grid-cols-[1fr_200px]">
            <div>
              <label
                htmlFor="customer-search"
                className="block text-sm font-medium text-text"
              >
                Search customers
              </label>

              <input
                id="customer-search"
                type="search"
                value={search}
                onChange={(event) => {
                  handleSearchChange(
                    event.target.value,
                  );
                }}
                placeholder="Search by name or email..."
                className="mt-2 w-full rounded-lg border border-border bg-background px-3 py-2 text-sm text-text outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/20"
              />
            </div>

            <div>
              <label
                htmlFor="customer-status"
                className="block text-sm font-medium text-text"
              >
                Status
              </label>

              <select
                id="customer-status"
                value={status}
                onChange={(event) => {
                  handleStatusChange(
                    event.target.value as
                      | CustomerStatus
                      | "all",
                  );
                }}
                className="mt-2 w-full rounded-lg border border-border bg-background px-3 py-2 text-sm text-text outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/20"
              >
                <option value="all">
                  All customers
                </option>

                <option value="active">
                  Active
                </option>

                <option value="inactive">
                  Inactive
                </option>
              </select>
            </div>
          </div>
        </Card>

        <div className="mt-8">
          {customersQuery.isLoading ? (
            <Card className="p-8 text-center">
              <p className="text-sm text-text-secondary">
                Loading customers...
              </p>
            </Card>
          ) : customersQuery.isError ? (
            <Card className="p-8 text-center">
              <p className="text-sm text-danger">
                Unable to load customers.
              </p>

              <Button
                type="button"
                variant="secondary"
                className="mt-4"
                onClick={() => {
                  void customersQuery.refetch();
                }}
              >
                Try Again
              </Button>
            </Card>
          ) : (
            <>
              <CustomerTable
                customers={customers}
                onDeactivate={
                  handleDeactivate
                }
                onActivate={
                  handleActivate
                }
                isDeactivating={
                  isUpdatingStatus
                }
              />

              <Card className="mt-4 p-4">
                <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                  <div className="text-sm text-text-secondary">
                    Showing {firstItem} to{" "}
                    {lastItem} of {total}{" "}
                    customers
                  </div>

                  <div className="flex flex-wrap items-center gap-3">
                    <label
                      htmlFor="customer-page-size"
                      className="text-sm text-text-secondary"
                    >
                      Per page
                    </label>

                    <select
                      id="customer-page-size"
                      value={size}
                      onChange={(event) => {
                        handlePageSizeChange(
                          Number(
                            event.target.value,
                          ),
                        );
                      }}
                      className="rounded-lg border border-border bg-background px-3 py-2 text-sm text-text outline-none focus:border-primary focus:ring-2 focus:ring-primary/20"
                    >
                      <option value={10}>
                        10
                      </option>

                      <option value={20}>
                        20
                      </option>

                      <option value={50}>
                        50
                      </option>

                      <option value={100}>
                        100
                      </option>
                    </select>

                    <Button
                      type="button"
                      variant="secondary"
                      disabled={isFirstPage}
                      onClick={() => {
                        setPage(
                          (current) =>
                            Math.max(
                              1,
                              current - 1,
                            ),
                        );
                      }}
                    >
                      Previous
                    </Button>

                    <span className="min-w-20 text-center text-sm font-medium text-text">
                      Page {page} of{" "}
                      {totalPages}
                    </span>

                    <Button
                      type="button"
                      variant="secondary"
                      disabled={isLastPage}
                      onClick={() => {
                        setPage(
                          (current) =>
                            Math.min(
                              totalPages,
                              current + 1,
                            ),
                        );
                      }}
                    >
                      Next
                    </Button>
                  </div>
                </div>
              </Card>
            </>
          )}
        </div>
      </Container>
    </Section>
  );
}