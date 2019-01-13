df = pd.read_table(r'C:\Codes\Snippets\sample data\alias.txt')


alias = {
    'filter':[
        "df['ppid'].isin(['a'])",
    ],
    'alias':[
        'ppid is A or C'
        'Other',
    ]
}


def apply_alias(df, alias):
    assert len(alias['filter']) == len(alias['alias'])-1, 'filter & alias length matching failed! filter: {0} - alias: {1}'.format(len(alias['filter']), len(alias['alias']))

    for i, val in enumerate(alias['filter']):
        df.loc[eval(val), 'alias'] = alias['alias'][i]

    df.loc[df['alias'].isnull(), 'alias'] = alias['alias'][len(alias['alias']) - 1]

    return df


if __name__ == '__main__':

    res = apply_alias(df, alias)

    res