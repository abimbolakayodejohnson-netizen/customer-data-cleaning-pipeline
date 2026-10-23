
import pandas as pd


# 1. Sample customer dataset
data = {
    "customer_id": ["C001", "C002", "C003", "C004",
                    "C005", "C006", "C007", "C008"],
    "name": ["  AMINA Yusuf ", "Kunle Ade", "chidi okafor",
             None, "Tobi Bello", "AMINA Yusuf",
             "Sade Bello", "  "],
    "age": ["25", "34", "-4", "150",
            "thirty", "25", "42", None],
    "email": ["amina@example.com", " kunle@gmail.com ",
              "chidi.example.com", None, "tobi@",
              "amina@example.com", "sade@gmail.com",
              "sade@gmail.com"],
    "city": ["ibadan", "LAGOS", "Ibadan", "abuja",
             "lagos", "Ibadan", " ibadan ", "IBADAN"]
}

df = pd.DataFrame(data)


# 2. Clean and standardize the data
def clean_customer_data(df):
    df = df.copy()

    df["name"] = df["name"].str.strip().str.title()
    df["city"] = df["city"].str.strip().str.title()
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["email"] = df["email"].str.strip()

    return df


# 3. Validate customer records
def standardize_customer_data(df):
    df = df.copy()

    df["valid_age"] = df["age"].between(0, 120)

    df["valid_email"] = (
        df["email"].str.contains("@", na=False)
        & ~df["email"].str.endswith("@", na=False)
    )

    df["valid_name"] = (
        df["name"].notna()
        & df["name"].str.strip().ne("")
    )

    return df


# 4. Detect duplicate email addresses
def remove_duplicates(validated_df):
    df = validated_df.copy()

    df["email_key"] = (
        df["email"].str.strip().str.lower()
    )

    duplicate_mask = (
        df.duplicated(subset=["email_key"], keep="first")
        & df["email_key"].notna()
    )

    unique_customers = df[~duplicate_mask].copy()
    duplicate_customers = df[duplicate_mask].copy()

    return unique_customers, duplicate_customers


# 5. Complete cleaning pipeline
def clean_customer_pipeline(df):
    cleaned_df = clean_customer_data(df)

    validated_df = standardize_customer_data(cleaned_df)

    unique_customers, duplicate_customers = (
        remove_duplicates(validated_df)
    )

    return validated_df, unique_customers, duplicate_customers


# 6. Generate a data-quality report
def create_quality_report(
    validated_df, unique_customers, duplicate_customers
):
    total = len(validated_df)

    report_dict = {
        "total_records": total,
        "missing_names": int(validated_df["name"].isna().sum()),
        "missing_ages": int(validated_df["age"].isna().sum()),
        "missing_emails": int(validated_df["email"].isna().sum()),
        "invalid_ages": int((~validated_df["valid_age"]).sum()),
        "invalid_emails": int((~validated_df["valid_email"]).sum()),
        "invalid_names": int((~validated_df["valid_name"]).sum()),
        "valid_age_percentage": round(
            validated_df["valid_age"].mean() * 100, 2
        ),
        "valid_email_percentage": round(
            validated_df["valid_email"].mean() * 100, 2
        ),
        "duplicate_records": len(duplicate_customers),
        "duplicate_percentage": round(
            len(duplicate_customers) / total * 100, 2
        ) if total else 0.0
    }

    return report_dict


# 7. Export the results
def save_dataframes(
    unique_customers, duplicate_customers, validated_df
):
    # Remove the internal comparison key from exported files
    unique_customers.drop(
        columns=["email_key"], errors="ignore"
    ).to_csv("unique_customers.csv", index=False)

    duplicate_customers.drop(
        columns=["email_key"], errors="ignore"
    ).to_csv("duplicate_customers.csv", index=False)

    validated_df.to_csv("validated_df.csv", index=False)

    print("\nCSV files saved successfully.")


# 8. Run the complete pipeline
if __name__ == "__main__":
    validated_df, unique_customers, duplicate_customers = (
        clean_customer_pipeline(df)
    )

    full_report = create_quality_report(
        validated_df, unique_customers, duplicate_customers
    )

    print("DATA QUALITY REPORT")
    for metric, value in full_report.items():
        print(f"{metric}: {value}")

    print("\nDUPLICATES FLAGGED FOR REVIEW")
    print(duplicate_customers[["customer_id", "email"]])

    save_dataframes(
        unique_customers, duplicate_customers, validated_df
    )
