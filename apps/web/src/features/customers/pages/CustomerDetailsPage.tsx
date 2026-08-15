import {
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";
import { useState } from "react";
import { Link, useParams } from "react-router-dom";

import Button from "@/components/ui/button";
import Card from "@/components/ui/card";
import Container from "@/components/ui/container";
import Section from "@/components/ui/section";
import { H1, Lead } from "@/components/ui/typography";

import { CustomerService } from "../api/customer.api";
import CustomerForm from "../components/CustomerForm";
import NotesSection from "../components/NotesSection";
import TasksSection from "../components/TaskSection";
import type { CustomerCreate } from "../types/customer.types";

export default function CustomerDetailsPage() {
  const { customerId } = useParams<{
    customerId: string;
  }>();

  const queryClient = useQueryClient();

  const [isEditing, setIsEditing] =
    useState(false);

  const customerQuery = useQuery({
    queryKey: ["customers", customerId],
    queryFn: () =>
      CustomerService.getCustomer(customerId!),
    enabled: Boolean(customerId),
  });

  const timelineQuery = useQuery({
    queryKey: [
      "customers",
      customerId,
      "timeline",
    ],
    queryFn: () =>
      CustomerService.getCustomerTimeline(
        customerId!,
      ),
    enabled: Boolean(customerId),
  });

  const updateCustomerMutation = useMutation({
    mutationFn: (data: CustomerCreate) =>
      CustomerService.updateCustomer(
        customerId!,
        data,
      ),

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: ["customers", customerId],
      });

      await queryClient.invalidateQueries({
        queryKey: [
          "customers",
          customerId,
          "timeline",
        ],
      });

      setIsEditing(false);
    },
  });

  if (!customerId) {
    return (
      <Section>
        <Container>
          <p className="text-text">
            Customer ID is missing.
          </p>

          <Link
            to="/customers"
            className="mt-4 inline-block"
          >
            <Button
              variant="secondary"
              type="button"
            >
              Back to Customers
            </Button>
          </Link>
        </Container>
      </Section>
    );
  }

  if (customerQuery.isLoading) {
    return (
      <Section>
        <Container>
          <p className="text-text-secondary">
            Loading customer...
          </p>
        </Container>
      </Section>
    );
  }

  if (
    customerQuery.isError ||
    !customerQuery.data
  ) {
    return (
      <Section>
        <Container>
          <p className="text-danger">
            Unable to load this customer.
          </p>

          <Link
            to="/customers"
            className="mt-4 inline-block"
          >
            <Button
              variant="secondary"
              type="button"
            >
              Back to Customers
            </Button>
          </Link>
        </Container>
      </Section>
    );
  }

  const customer = customerQuery.data;

  return (
    <Section>
      <Container>
        <Link
          to="/customers"
          className="text-sm text-text-secondary hover:text-text"
        >
          ← Back to Customers
        </Link>

        <div className="mt-6 flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
          <div>
            <H1>
              {customer.first_name}{" "}
              {customer.last_name}
            </H1>

            <Lead className="mt-3">
              Customer profile, notes, tasks,
              and activity timeline.
            </Lead>
          </div>

          {!isEditing && (
            <Button
              type="button"
              onClick={() =>
                setIsEditing(true)
              }
            >
              Edit Customer
            </Button>
          )}
        </div>

        {updateCustomerMutation.isError && (
          <div className="mt-6 rounded-lg border border-red-200 bg-red-50 p-4">
            <p className="text-sm text-danger">
              Unable to update this customer.
              Please try again.
            </p>
          </div>
        )}

        {isEditing ? (
          <div className="mt-10">
            <div className="mb-4">
              <h2 className="text-lg font-semibold text-text">
                Edit Customer
              </h2>

              <p className="mt-1 text-sm text-text-secondary">
                Update the customer's
                information below.
              </p>
            </div>

            <CustomerForm
              initialValues={{
                first_name:
                  customer.first_name,
                last_name:
                  customer.last_name,
                email: customer.email,
                phone: customer.phone,
              }}
              onSubmit={(data) =>
                updateCustomerMutation.mutate(
                  data,
                )
              }
              isSubmitting={
                updateCustomerMutation.isPending
              }
              submitLabel="Save Changes"
              submittingLabel="Saving..."
              onCancel={() => {
                setIsEditing(false);
                updateCustomerMutation.reset();
              }}
            />
          </div>
        ) : (
          <div className="mt-10 space-y-6">
            <div className="grid gap-6 lg:grid-cols-2">
              <Card className="p-6">
                <h2 className="text-lg font-semibold text-text">
                  Customer Information
                </h2>

                <dl className="mt-6 space-y-4">
                  <div>
                    <dt className="text-sm text-text-secondary">
                      Email
                    </dt>

                    <dd className="mt-1 text-sm font-medium text-text">
                      {customer.email}
                    </dd>
                  </div>

                  <div>
                    <dt className="text-sm text-text-secondary">
                      Phone
                    </dt>

                    <dd className="mt-1 text-sm font-medium text-text">
                      {customer.phone ??
                        "—"}
                    </dd>
                  </div>

                  <div>
                    <dt className="text-sm text-text-secondary">
                      Status
                    </dt>

                    <dd className="mt-1 text-sm font-medium capitalize text-text">
                      {customer.status}
                    </dd>
                  </div>

                  <div>
                    <dt className="text-sm text-text-secondary">
                      Created
                    </dt>

                    <dd className="mt-1 text-sm font-medium text-text">
                      {new Date(
                        customer.created_at,
                      ).toLocaleString()}
                    </dd>
                  </div>

                  <div>
                    <dt className="text-sm text-text-secondary">
                      Last Updated
                    </dt>

                    <dd className="mt-1 text-sm font-medium text-text">
                      {new Date(
                        customer.updated_at,
                      ).toLocaleString()}
                    </dd>
                  </div>
                </dl>
              </Card>

              <Card className="p-6">
                <h2 className="text-lg font-semibold text-text">
                  Activity Timeline
                </h2>

                <div className="mt-6">
                  {timelineQuery.isLoading && (
                    <p className="text-sm text-text-secondary">
                      Loading timeline...
                    </p>
                  )}

                  {timelineQuery.isError && (
                    <p className="text-sm text-danger">
                      Unable to load timeline.
                    </p>
                  )}

                  {!timelineQuery.isLoading &&
                    !timelineQuery.isError &&
                    timelineQuery.data
                      ?.length === 0 && (
                      <p className="text-sm text-text-secondary">
                        No activity recorded
                        yet.
                      </p>
                    )}

                  <div className="space-y-6">
                    {timelineQuery.data?.map(
                      (activity) => (
                        <div
                          key={activity.id}
                          className="border-l-2 border-border pl-4"
                        >
                          <p className="text-sm font-medium text-text">
                            Customer{" "}
                            {activity.action}
                          </p>

                          <p className="mt-1 text-sm text-text-secondary">
                            Customer record was{" "}
                            {activity.action}.
                          </p>

                          {activity.actor_id && (
                            <p className="mt-1 text-xs text-text-secondary">
                              Actor:{" "}
                              {activity.actor_id}
                            </p>
                          )}

                          <p className="mt-2 text-xs text-text-secondary">
                            {new Date(
                              activity.created_at,
                            ).toLocaleString()}
                          </p>
                        </div>
                      ),
                    )}
                  </div>
                </div>
              </Card>
            </div>

            <div className="grid gap-6 lg:grid-cols-2">
              <NotesSection
                customerId={customerId}
              />

              <TasksSection
                customerId={customerId}
              />
            </div>
          </div>
        )}
      </Container>
    </Section>
  );
}