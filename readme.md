# e-Tetika Web App (electronic - estetika dan etika)
## For Hackathon Samamarinda 3.0

### Page scheme
1. account
 - register
 - login
 - profile


2. article
 - blog (crud article)
 - detail article

3. event
 - crud event
 - search event
 - detail event
 - watch event (if online)

4. cart
 - crud cart
 - detail order
 - checkout

5. product (sell product retail)
 - crud product
 - search product

### Data scheme
1. account (user get user in django)
 - id pk auto_increment
 - username (string, unique)
 - password (string)
 - name (string)
 - group_name (string)
 - email (string, unique)
 - no_hp (string, unique)
 - is_performer (bool)
 - group_category (string)
 - is_partner (boolean)
 - profile_picture (ImageField)

2. article
 - id pk auto_increment
 - title (string)
 - overview (string)
 - content (string)
 - datetime (string)
 - slug (slugField)
 - picture (if in frontpage resize to thumbnail) (ImageField)
 - status -> STATUS_CHOICES a. draft b. published
 - author (string) -> foregin key oneToOne user

3. event
 - id pk auto_increment
 - title (string)
 - overview (string)
 - banner (imageField)
 - picture (imageField)
 - location (string)
 - datetime (string)
 - quota (string)
 - is_refund (boolean)
 - other_artist (string)
 - ticket_price (fk from cart)
 - quantity (fk from cart)
 - id_user (fk from user)

4. cart
 - id pk auto_increment
 - datetime
 - quantity
 - name
 - description
 - price
 - id_user (fk from user)
 - sub_total

5. product retail
 - id pk auto_increment
 - datetime
 - quantity
 - name
 - description
 - price
 - weight
 - shippingFee
 - id_user (fk from user)

### User and Permission
1. Superadmin
  - All pages write and read

2. user -> is_partner true
 - can sell product
 - can create article
 - only if is performer true
 - must fill group_name

3. user -> is_peformer true
 - can create event
 - can create article
 - must fill group_name

4. user only
 - only can buy ticket
